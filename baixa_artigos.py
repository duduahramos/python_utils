#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Converte uma lista de URLs (HTML) para arquivos Markdown usando Docling.

Uso:
  python html2md_docling.py --urls urls.txt --out ./md_out --workers 6
  python html2md_docling.py --url https://example.com --out ./md_out
"""

import argparse
import concurrent.futures as cf
import hashlib
import os
import sys
import tempfile
from pathlib import Path
from typing import Iterable, List, Optional
from urllib.parse import urlparse

import requests
from docling.document_converter import DocumentConverter  # docling
from slugify import slugify
from tqdm import tqdm


def read_urls(args) -> List[str]:
    urls: List[str] = []
    if args.url:
        urls.append(args.url.strip())
    if args.urls:
        with open(args.urls, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    urls.append(s)
    if not urls and not sys.stdin.isatty():
        # permite: cat urls.txt | python html2md_docling.py --out md
        for line in sys.stdin:
            s = line.strip()
            if s and not s.startswith("#"):
                urls.append(s)
    # dedup preservando ordem
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            deduped.append(u)
            seen.add(u)
    return deduped


def safe_name_from_url(u: str) -> str:
    """
    Gera um nome de arquivo estável e legível a partir da URL.
    Ex.: https://site.com/path?a=1 -> site-com-path-<hash8>.md
    """
    p = urlparse(u)
    base = "-".join([p.netloc.replace(".", "-"), slugify(p.path or "index") or "index"])
    h = hashlib.sha256(u.encode("utf-8")).hexdigest()[:8]
    return f"{base}-{h}.md"


def fetch_to_tempfile(url: str) -> Optional[str]:
    """
    Fallback: baixa o HTML para um arquivo temporário, caso o fetch interno do Docling falhe
    (alguns hosts bloqueiam user-agents).
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; DoclingFetcher/1.0; +https://github.com/docling-project/docling)"
        }
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        # Aceita HTML mesmo sem content-type perfeito
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
        tmp.write(r.content)
        tmp.flush()
        tmp.close()
        return tmp.name
    except Exception:
        return None


def convert_one(url: str, out_dir: Path, converter: DocumentConverter, add_front_matter: bool = True) -> dict:
    """
    Converte uma URL (ou arquivo HTML temporário) para Markdown.
    Retorna dict com status e caminho do arquivo.
    """
    out_path = out_dir / safe_name_from_url(url)

    try:
        # 1) tenta converter direto da URL (Docling aceita URL como 'source')
        result = converter.convert(url)
        md = result.document.export_to_markdown()
    except Exception:
        # 2) fallback: baixa HTML manualmente e converte do arquivo local
        tmpfile = fetch_to_tempfile(url)
        if not tmpfile:
            raise
        try:
            result = converter.convert(tmpfile)
            md = result.document.export_to_markdown()
        finally:
            try:
                os.unlink(tmpfile)
            except Exception:
                pass

    if add_front_matter:
        # front matter simples com metadados básicos
        fm = [
            "---",
            f"title: \"{url}\"",
            f"source_url: \"{url}\"",
            "---",
            "",
        ]
        md = "\n".join(fm) + md

    out_path.write_text(md, encoding="utf-8")
    return {"url": url, "file": str(out_path), "ok": True}


def run(urls: Iterable[str], out_dir: str, workers: int) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    converter = DocumentConverter()  # pronto para converter URLs/arquivos

    results = []
    errors = []

    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(convert_one, u, out, converter): u for u in urls}
        for fut in tqdm(cf.as_completed(futures), total=len(futures), desc="Convertendo"):
            u = futures[fut]
            try:
                results.append(fut.result())
            except Exception as e:
                errors.append((u, repr(e)))

    # índice simples
    index_path = Path(out) / "_index.csv"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("url,file,ok\n")
        for r in results:
            f.write(f"{r['url']},{r['file']},{r['ok']}\n")
        for u, e in errors:
            f.write(f"{u},,False\n")

    print(f"\n✅ Sucesso: {len(results)} | ❌ Falhas: {len(errors)} | Índice: {index_path}")
    if errors:
        print("Algumas falhas (mostrando até 5):")
        for u, e in errors[:5]:
            print(f"  - {u} -> {e}")


def main():
    ap = argparse.ArgumentParser(description="Converte HTML (via URLs) para Markdown usando Docling.")
    ap.add_argument("--url", help="Uma única URL para converter.")
    ap.add_argument("--urls", help="Arquivo .txt com uma URL por linha.")
    ap.add_argument("--out", default="./md_out", help="Diretório de saída (padrão: ./md_out).")
    ap.add_argument("--workers", type=int, default=4, help="Número de conversões em paralelo (default: 4).")
    args = ap.parse_args()

    urls = read_urls(args)
    if not urls:
        print("Nenhuma URL fornecida. Use --url, --urls ou stdin.", file=sys.stderr)
        sys.exit(1)

    run(urls, args.out, args.workers)


if __name__ == "__main__":
    main()
