---
title: "https://medium.com/xp-inc/design-patterns-parte-14-proxy-9f72c15a2ee1"
source_url: "https://medium.com/xp-inc/design-patterns-parte-14-proxy-9f72c15a2ee1"
---
# Design Patterns - Parte 14 - Proxy

Jones Roberto Nuzzi4 min read·Dec 3, 2019

--

1

Share

<!-- image -->

# Intenção

Proxy é um padrão de design estrutural que permite fornecer um substituto ou espaço reservado para outro objeto. Um proxy controla o acesso ao objeto original, permitindo que você execute algo antes ou depois que a solicitação chega ao objeto original.

# Problema

Você precisa oferecer suporte a objetos com fome de recursos e não deseja instanciar esses objetos, a menos e até que eles sejam realmente solicitados pelo cliente.

# Solução

O padrão Proxy sugere que você crie uma nova classe de proxy com a mesma interface que um objeto de serviço original. Em seguida, você atualiza seu aplicativo para que ele transmita o objeto proxy para todos os clientes do objeto original. Ao receber uma solicitação de um cliente, o proxy cria um objeto de serviço real e delega todo o trabalho para ele.

<!-- image -->

O proxy se disfarça de objeto de banco de dados. Ele pode lidar com inicialização lenta e cache de resultados sem o cliente ou o objeto de banco de dados real saiba.

Mas qual é o benefício? Se você precisar executar algo antes ou depois da lógica primária da classe, o proxy permitirá fazer isso sem alterar essa classe. Como o proxy implementa a mesma interface que a classe original, ele pode ser passado para qualquer cliente que espera um objeto de serviço real.

# Implementação

O diagrama de classes UML para a implementação do padrão de design do proxy é fornecido abaixo:

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Subject

Essa é uma interface com membros que serão implementados pelas classes RealSubject e Proxy.

## RealSubject

Esta é uma classe que queremos usar com mais eficiência usando a classe proxy.

## Proxy

Esta é uma classe que contém a instância da classe RealSubject e pode acessar os membros da classe RealSubject, conforme necessário.

# Prós

- Você pode controlar o objeto de serviço sem que os clientes saibam disso.
- Você pode gerenciar o ciclo de vida do objeto de serviço quando os clientes não se importam com isso.
- O proxy funciona mesmo se o objeto de serviço não estiver pronto ou não estiver disponível.
- Princípio Aberto / Fechado . Você pode introduzir novos proxies sem alterar o serviço ou os clientes.

# Contras

- O código pode se tornar mais complicado, pois você precisa introduzir muitas novas classes.
- A resposta do serviço pode demorar.

# Exemplo

## Uso do padrão em C#

<!-- image -->

## Quem é o que

As classes, interfaces e objetos no diagrama de classes acima podem ser identificados da seguinte maneira:

IClient- interface Subject.

RealClient - classe RealSubject.

ProxyClient - classe Proxy.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos lá, vou tentar dar um exemplo simples e direto. Vou começar criando a interface IClient que será nosso subject e ela irá conter o seguinte código:

```
public interface IClient{string GetData();}
```

Em seguida irei adicionar classe RealSubject que irá implementar IClient, e ela irá conter o seguinte código:

```
public class RealClient : IClient{string Data;public RealClient(){Console.WriteLine("Real Client: Initialized");Data = "XP Inc. Medium";}public string GetData(){return Data;}}
```

Em seguida iremos criar nosso proxy, e a classe irá conter o seguinte código:

```
public class ProxyClient : IClient{RealClient client = new RealClient();public ProxyClient(){Console.WriteLine("ProxyClient: Initialized");}public string GetData(){return client.GetData();}}
```

E por último vamos modificar no Program.cs, e ele ficará com o seguinte código:

```
class Program{static void Main(string[] args){var proxy = new ProxyClient();Console.WriteLine($"Data from Proxy Client = {proxy.GetData()}");Console.WriteLine("Press any key to close!");Console.ReadKey();}}
```

Bom pessoal, em todos os posts estou tentando simplificar os exemplos, vou ficando por aqui, não deixe de acompanhar a postagem da semana que vem irei falar do próximo pattern da lista.

Não esqueça que os exemplos estão no Github. Abraço, até mais pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Xp IncXp InvestimentosLab XpDesign Patterns

--

--

1

## Written by Jones Roberto Nuzzi

559 followers·18 following

CTO na KYVA!, Sempre focado em desenvolvimento de sistemas para o mercado financeiro, com mais de 15 anos de experiência!

## Responses ( 1 )

See all responses

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