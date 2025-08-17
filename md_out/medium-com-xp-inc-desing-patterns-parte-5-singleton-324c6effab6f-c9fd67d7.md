---
title: "https://medium.com/xp-inc/desing-patterns-parte-5-singleton-324c6effab6f"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-5-singleton-324c6effab6f"
---
# Design Patterns - Parte 5 - Singleton

Jones Roberto Nuzzi4 min read·Oct 22, 2019

--

Share

<!-- image -->

# Intenção

Singleton é um padrão de design criacional, que garante que apenas um objeto desse tipo exista e forneça um único ponto de acesso a ele para qualquer outro código.

# Problema

O aplicativo precisa de uma e apenas uma instância de um objeto. Além disso, inicialização lenta e acesso global são necessários.

O padrão Singleton resolve dois problemas ao mesmo tempo:

1- Certifique-se de que uma classe tenha apenas uma única instância . Por que alguém iria querer controlar quantas instâncias uma classe possui? O motivo mais comum para isso é controlar o acesso a algum recurso compartilhado - por exemplo, um banco de dados ou um arquivo.

- Eis como funciona: imagine que você criou um objeto, mas depois de um tempo decidiu criar um novo. Em vez de receber um objeto novo, você obterá o que você já criou.
- Observe que esse comportamento é impossível de implementar com um construtor comum, pois uma chamada de construtor sempre deve retornar um novo objeto por design.

2-Forneça um ponto de acesso global para essa instância . Lembra-se daquelas variáveis globais que você (eu também fazia..rsrs) costumava armazenar alguns objetos essenciais? Embora sejam muito úteis, também são muito inseguros, pois qualquer código pode sobrescrever o conteúdo dessas variáveis e travar o aplicativo.

- Assim como uma variável global, o padrão Singleton permite acessar algum objeto de qualquer lugar do programa. No entanto, também protege essa instância de ser substituída por outro código.
- Há um outro lado desse problema: você não deseja que o código que foi criado para resolver o problema nº 1 seja espalhado por todo o programa. É muito melhor tê-lo em uma classe, especialmente se o resto do seu código já depende dele.

Atualmente, o padrão Singleton se tornou tão popular que as pessoas podem chamar algo de singleton, mesmo que resolva apenas um dos problemas listados.

# Solução

Torne a classe do objeto de instância única responsável pela criação, inicialização, acesso e aplicação. Declare a instância como um membro de dados private static. Forneça uma função de membro public static que encapsule todo o código de inicialização e forneça acesso à instância.

O cliente chama o método usando o nome da classe e o método singleton sempre que uma referência à instância única é necessária.

# Implementação

<!-- image -->

As classes e objetos no diagrama de classes UML acima são os seguintes:

## Singleton

Essa é uma classe responsável por criar e manter sua própria instância exclusiva.

# Prós

- Você pode ter certeza de que uma classe possui apenas uma única instância.
- Você ganha um ponto de acesso global para essa instância.
- O objeto singleton é inicializado somente quando solicitado pela primeira vez.

# Contras

- Viola o princípio da responsabilidade única. O padrão resolve dois problemas no momento.
- O padrão requer tratamento especial em um ambiente multithread para que vários threads não criem um objeto singleton várias vezes.
- Pode ser difícil testar o código do cliente do Singleton, porque muitas estruturas de teste dependem da herança ao produzir objetos simulados. Como o construtor da classe singleton é privado e a substituição de métodos estáticos é impossível na maioria das linguagens, você precisará pensar em uma maneira criativa de testar o seu singleton. Ou simplesmente não escreva os testes. Ou não use o padrão Singleton.

# Exemplo

<!-- image -->

É muito fácil implementar um Singleton desleixado. Você só precisa ocultar o construtor e implementar um método de criação estático.

A mesma classe se comporta incorretamente em um ambiente multithread. Vários threads podem chamar o método de criação simultaneamente e obter várias instâncias da classe Singleton.

```
class SingletonWrong{private SingletonWrong() { }private static SingletonWrong _instance;public static SingletonWrong GetInstance(){if (_instance == null){_instance = new SingletonWrong();}return _instance;}public static void SomeBusinessLogic(){}}
```

Para corrigir o problema, você deve sincronizar os threads durante a primeira criação do objeto Singleton.

```
class SingletonThreadSafe{private SingletonThreadSafe() { }private static SingletonThreadSafe _instance;// We now have a lock object that will be used to synchronize threads// during first access to the Singleton.private static readonly object _lock = new object();public static SingletonThreadSafe GetInstance(string value){// This conditional is needed to prevent threads stumbling over the// lock once the instance is ready.if (_instance == null){lock (_lock){if (_instance == null){_instance = new SingletonThreadSafe();_instance.Value = value;}}}return _instance;}public string Value { get; set; }}
```

# Quer saber mais?

Existem ainda mais sabores especiais do padrão Singleton em C #. Dê uma olhada neste artigo para descobrir mais:

Implementing the Singleton Pattern in C#

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Xp IncXp InvestimentosLabxpDesign Patterns

--

--

## Written by Jones Roberto Nuzzi

559 followers·18 following

CTO na KYVA!, Sempre focado em desenvolvimento de sistemas para o mercado financeiro, com mais de 15 anos de experiência!

## No responses yet

Help

Status

About

Careers

Press

Blog

Privacy

Rules

Terms

Text to speech