---
title: "https://medium.com/xp-inc/design-patterns-parte-15-chain-of-resposability-8790ebb5d443"
source_url: "https://medium.com/xp-inc/design-patterns-parte-15-chain-of-resposability-8790ebb5d443"
---
# Design Patterns - Parte 15 - Chain of responsibility

Jones Roberto Nuzzi5 min read·Dec 10, 2019

--

1

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite passar solicitações ao longo de uma cadeia de manipuladores. Ao receber uma solicitação, cada manipulador decide processar a solicitação ou passá-la para o próximo manipulador na cadeia.

# Problema

Ao escrever um aplicativo de qualquer tipo, geralmente acontece que o evento gerado por um objeto precisa ser tratado por outro. E, para tornar nosso trabalho ainda mais difícil, também temos acesso negado ao objeto que precisa lidar com o evento.

# Solução

O padrão de design da Chain of Responsibility permite que um objeto envie um comando sem saber qual objeto receberá e manipulará. A solicitação é enviada de um objeto para outro, tornando-os partes de uma cadeia e cada objeto dessa cadeia pode manipular o comando, transmiti-lo ou fazer os dois. O exemplo mais comum de uma máquina que usa a Cadeia de Responsabilidade é o slot para moedas da máquina de venda automática: em vez de ter um slot para cada tipo de moeda, a máquina possui apenas um slot para todos eles. A moeda descartada é roteada para o local de armazenamento apropriado, determinado pelo receptor do comando.

# Implementação

O diagrama de classes UML para a implementação do padrão de design da cadeia de responsabilidades é apresentado abaixo:

<!-- image -->

## Client

Essa é a classe que gera a solicitação e a passa para o primeiro manipulador na cadeia de responsabilidade.

## Handler

Esta é a classe abstrata que contém um membro que mantém o próximo manipulador na cadeia e um método associado para definir esse sucessor. Ele também possui um método abstrato que deve ser implementado por classes concretas para manipular a solicitação ou passá-la para o próximo objeto no pipeline.

## ConcreteHandlerA &amp; ConcreteHandlerB

Essas são classes de concretas de manipuladores que são herdadas da classe Handler. Isso inclui a funcionalidade de lidar com algumas solicitações e passar outras para o próximo item na cadeia de solicitações.

# Prós

- Você pode controlar a ordem de tratamento de solicitações.
- Princípio de responsabilidade única . Você pode desacoplar classes que invocam operações de classes que executam operações.
- Princípio Aberto/Fechado . Você pode introduzir novos manipuladores no aplicativo sem quebrar o código do cliente existente.

# Contras

- Alguns pedidos podem acabar sem tratamento.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

As classes, interfaces e objetos no diagrama de classes podem ser identificados da seguinte maneira:

1. Approver- classe abstrata do manipulador.
2. Clerk, Assistant Manager &amp; Manager- classes ConcreteHandler.
3. Loan &amp; LoanEventArgs - Essas classes são usadas para processamento interno e mantêm os detalhes da solicitação.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos lá, conforme mostrado na imagem acima esse padrão não é tão popular, e por isso irei tentar criar um exemplo simples. Nesse exemplo irei simular uma cadeia de aprovação de empréstimos.Vou começar criando as classes de manipulação do Evento de empréstimo, meu projeto ficou com o seguinte formato:

<!-- image -->

A classe Loan irá conter o seguinte código:

```
public class Loan{public decimal Amount { get; set; }public string Purpose { get; set; }public int Number { get; set; }}
```

em seguida irei criar a classe LoanEventArgs, que será usada pelo nosso Handler, que irá conter o seguinte código:

```
public class LoanEventArgs : EventArgs{internal Loan Loan { get; set; }}
```

Bom, agora iremos criar nosso handler, irei nomear de Approver, e irá conter o seguinte código:

```
public abstract class Approver{// Loan eventpublic EventHandler<LoanEventArgs> Loan;// Loan event handlerpublic abstract void LoanHandler(object sender, LoanEventArgs e);// Constructorpublic Approver(){Loan += LoanHandler;}public void ProcessRequest(Loan loan){OnLoan(new LoanEventArgs { Loan = loan });}// Invoke the Loan eventpublic virtual void OnLoan(LoanEventArgs e){if (Loan != null){Loan(this, e);}}// Sets or gets the next approverpublic Approver Successor { get; set; }}
```

Agora irei criar 3 classes de serão ConcreteHandlers,serão elas:

- AssistantManager (que irá representar um assistente da gerência)

```
class AssistantManager : Approver{public override void LoanHandler(object sender, LoanEventArgs e){if (e.Loan.Amount < 45000){Console.WriteLine($"{GetType().Name} approved request# {e.Loan.Number}");}else if (Successor != null){Successor.LoanHandler(this, e);}}}
```

- Clerk (que irá representar um escrivão)

```
class Clerk : Approver{public override void LoanHandler(object sender, LoanEventArgs e){if (e.Loan.Amount < 25000){Console.WriteLine($"{GetType().Name} approved request# {e.Loan.Number}");}else if (Successor != null){Successor.LoanHandler(this, e);}}}
```

- Manager ( que será nosso gerente)

```
class Manager : Approver{public override void LoanHandler(object sender, LoanEventArgs e){if (e.Loan.Amount < 100000){Console.WriteLine($"{GetType().Name} approved request# {e.Loan.Number}");}else if (Successor != null){Successor.LoanHandler(this, e);}else{Console.WriteLine("Request# {0} requires an executive meeting!",e.Loan.Number);}}}
```

E por fim a nossa classe Program.cs será modificada para ser nosso Client, e ela irá conter o seguinte código:

```
class Program{static void Main(string[] args){Approver diego = new Clerk();Approver cesar = new AssistantManager();Approver jones = new Manager();diego.Successor = cesar;cesar.Successor = jones;// Generate and process loan requestsvar loan = new Loan { Number = 2034, Amount = 23000, Purpose = "Car Loan" };diego.ProcessRequest(loan);loan = new Loan { Number = 2035, Amount = 44500, Purpose = "Motorcycle Loan" };diego.ProcessRequest(loan);loan = new Loan { Number = 2036, Amount = 156200, Purpose = "Apartament Loan" };diego.ProcessRequest(loan);Console.WriteLine("Press any key to continue!");Console.ReadKey();}}
```

Bom pessoal, lembrando que todos os exemplos podem ser encontrados no meu github, e o link encontra-se logo ao fim da postagem. Vou ficando por aqui, não perca meu próximo artigo onde irei trazer mais um dos 23 padrões do GOF; Abraço e até mais..

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsXp IncXp InvestimentosCsharp

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