---
title: "https://medium.com/xp-inc/desing-patterns-parte-9-bridge-5ca127f72de"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-9-bridge-5ca127f72de"
---
# Design Patterns - Parte 9 - Bridge

Jones Roberto Nuzzi5 min read·Nov 12, 2019

--

Share

<!-- image -->

# Intenção

Bridge é um padrão de design estrutural que permite dividir uma classe grande ou um conjunto de classes estreitamente relacionadas em duas hierarquias separadas - abstração e implementação - que podem ser desenvolvidas independentemente uma da outra.

# Problema

Abstração? Implementação? Parece assustador? Fique calmo e vamos considerar um exemplo simples.

Digamos que você tenha uma classe chamada Shape com um par de subclasses: Circle e Square. Você deseja estender essa hierarquia de classes para incorporar cores, e planeja criar Red e Blue modelar subclasses. No entanto, como você já tem duas subclasses, precisará criar quatro combinações de classes, como BlueCircle e RedSquare.

<!-- image -->

O número de combinações de classes cresce em progressão geométrica.

Adicionar novos tipos de formas e cores à hierarquia aumentará exponencialmente. Por exemplo, para adicionar uma forma de triângulo, é necessário introduzir duas subclasses, uma para cada cor. E depois disso, adicionar uma nova cor exigiria a criação de três subclasses, uma para cada tipo de forma. Quanto mais avançamos, pior fica.

# Solução

Esse problema ocorre porque estamos tentando estender as classes de forma em duas dimensões independentes: por forma e por cor. Esse é um problema muito comum na herança de classes.

O padrão Bridge tenta resolver esse problema alternando da herança para a composição do objeto. O que isso significa é que você extrai uma das dimensões em uma hierarquia de classes separada, para que as classes originais façam referência a um objeto da nova hierarquia, em vez de ter todos os seus estados e comportamentos em uma classe.

<!-- image -->

Você pode impedir a explosão de uma hierarquia de classes, transformando-a em várias hierarquias relacionadas.

Seguindo essa abordagem, podemos extrair o código relacionado à cor em sua própria classe com duas subclasses: Red e Blue . A classe Shape obtém um campo de referência apontando para um dos objetos de cores. Agora a forma pode delegar qualquer trabalho relacionado a cores no objeto de cor vinculado. Essa referência atuará como uma ponte(Bridge) entre as classes Shape e Color. A partir de agora, adicionar novas cores não exigirá alterações na hierarquia de formas e vice-versa.

# Implementação

O diagrama de classes UML para a implementação do padrão de design Bridge é fornecido abaixo

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Abstraction

Esta é uma classe abstrata e contém membros que definem um objeto de negócios abstrato e sua funcionalidade. Ele contém uma referência a um objeto do tipo Bridge. Também pode atuar como a classe base para outras abstrações.

## Redefined Abstraction

Esta é uma classe que herda da classe Abstraction. Estende a interface definida pela classe Abstraction.

## Bridge

Essa é uma interface que atua como uma ponte entre a classe de abstração e as classes do implementador e também torna a funcionalidade da classe do implementador independente da classe de abstração.

## ImplementationClass

Essas são classes que implementam a interface Bridge e também fornecem os detalhes de implementação para a classe Abstraction associada.

# Prós

- Você pode criar classes e aplicativos independentes de plataforma.
- O código do cliente funciona com abstrações de alto nível. Não é exposto aos detalhes da plataforma.
- Princípio Aberto/Fechado . Você pode introduzir novas abstrações e implementações independentemente uma da outra.
- Princípio de responsabilidade única . Você pode se concentrar na lógica de alto nível na abstração e nos detalhes da plataforma na implementação.

# Contras

Você pode tornar o código mais complicado aplicando o padrão a uma classe altamente coesa.

# Exemplo

## Uso do padrão em C#

<!-- image -->

## O que é oque?

Message - Classe Abstraction .

SystemMessage e UserMessage- Classes RedefinedAbstraction.

IMessageSender- Interface Bridge.

EmailSender, WebServiceSender e MSMQ Sender- ImplementationClass que implementam a interface IMessageSender.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Vamos primeiramente criar a classe Abstraction ela irá se chamar Message, ela deverá conter o seguinte código:

```
public abstract class Message{public IMessageSender MessageSender { get; set; }public string Subject { get; set; }public string Body { get; set; }public abstract void Send();}
```

Em seguida iremos adicionar a classe RefinedAbstraction ela irá se chamar SystemMessage e irá herdar da classe Abstraction, ela deverá ter o seguinte código:

```
public class SystemMessage : Message{public override void Send(){MessageSender.SendMessage(Subject, Body);}}
```

Em seguida iremos adicionar a classe RefinedAbstraction ela irá se chamar UserMessage e irá herdar da classe Abstraction, ela deverá ter o seguinte código:

```
public class UserMessage : Message{public string UserComments { get; set; }public override void Send(){string fullBody = string.Format("{0}\nUser Comments: {1}", Body, UserComments);MessageSender.SendMessage(Subject, fullBody);}}
```

agora iremos criar a interface Bridge ela irá se chamar IMessageSender, e irá conter o seguinte código:

```
public interface IMessageSender{void SendMessage(string subject, string body);}
```

na sequência iremos adicionar a classe Concreta que irá implementar nosso IMessageSender, o nome dela será EmailSender, e irá conter o seguinte código:

```
public class EmailSender : IMessageSender{public void SendMessage(string subject, string body){Console.WriteLine($"Email\n{subject}\n{body}\n");}}
```

agora iremos adicionar mais uma classe Concreta que também irá implementar nosso IMessageSender, o nome será MSMQSender, e irá conter o seguinte código:

```
public class MSMQSender : IMessageSender{public void SendMessage(string subject, string body){Console.WriteLine($"MSMQ\n{subject}\n{body}\n");}}
```

e agora no final iremos adicionar uma terceira classe concreta que também implementa IMessageSender, com o nome WebServiceSender, e irá conter o seguinte código:

```
public class WebServiceSender : IMessageSender{public void SendMessage(string subject, string body){Console.WriteLine($"Web Service\n{subject}\n{body}\n");}}
```

Agora iremos modificar nossa classe Program para conseguirmos testar o nosso exemplo de Bridge, ela ficará com seguinte código:

```
class Program{static void Main(string[] args){IMessageSender email = new EmailSender();IMessageSender queue = new MSMQSender();IMessageSender web = new WebServiceSender();Message message = new SystemMessage();message.Subject = "Mensagem teste";message.Body = "Olá, Essa é uma mensagem de teste";message.MessageSender = email;message.Send();message.MessageSender = queue;message.Send();message.MessageSender = web;message.Send();UserMessage usermsg = new UserMessage();usermsg.Subject = "Mensagem Teste";usermsg.Body = "Olá, Essa é uma mensagem de teste";usermsg.UserComments = "Espero que todos consigam fazer o exemplo";usermsg.MessageSender = email;usermsg.Send();Console.ReadKey();}}
```

Bom, vou ficando por aqui em breve trarei mais um pattern para vocês,

Abraço, até mais

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsChsarpXpincXp Investimentos

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