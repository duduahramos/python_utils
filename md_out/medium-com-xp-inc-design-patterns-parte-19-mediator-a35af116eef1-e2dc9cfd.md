---
title: "https://medium.com/xp-inc/design-patterns-parte-19-mediator-a35af116eef1"
source_url: "https://medium.com/xp-inc/design-patterns-parte-19-mediator-a35af116eef1"
---
# Design Patterns - Parte 19 - Mediator

Jones Roberto Nuzzi4 min read·Jan 10, 2020

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite reduzir dependências caóticas entre objetos. O padrão restringe as comunicações diretas entre os objetos e os força a colaborar apenas por meio de um objeto mediador.

# Problema

Queremos projetar componentes reutilizáveis, mas as dependências entre as peças potencialmente reutilizáveis demonstram o fenômeno "código espaguete" (tentar colher uma única porção resulta em um "conjunto de tudo ou nada").

# Solução

O padrão mediator sugere que você interrompa toda a comunicação direta entre os componentes que deseja tornar independentes um do outro. Em vez disso, esses componentes devem colaborar indiretamente, chamando um objeto mediator especial que redireciona as chamadas para os componentes apropriados. Como resultado, os componentes dependem apenas de uma única classe de mediator em vez de serem acoplados a dezenas de classes.

# Implementação

O diagrama de classes UML para a implementação do Padrão de Design do Mediador é apresentado abaixo:

<!-- image -->

# Prós

- Princípio de responsabilidade única . Você pode extrair as comunicações entre vários componentes em um único local, facilitando a compreensão e a manutenção.
- Princípio Aberto / Fechado . Você pode introduzir novos mediadores sem precisar alterar os componentes reais.
- Você pode reduzir o acoplamento entre vários componentes de um programa.
- Você pode reutilizar componentes individuais mais facilmente.

# Contras

Com o tempo, um mediator pode evoluir para um Objeto Divino.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Mediator

Essa é uma interface que define operações que podem ser chamadas pelos objetos colegas para comunicação.

## ConcreteMediator

Esta é uma classe que implementa as operações de comunicação da interface do Mediador.

## Colleague

Esta é uma classe que define um único campo protegido que mantém uma referência a um mediador.

## ConcreteColleagueA / B

Estas são as classes que se comunicam através do mediador.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos para o nosso exemplo, como sempre vou tentar criar um exemplo mais simples possível, lembrando que nem sempre é possível.

Primeiramente irei criar a interface IMediator, que irá conter o seguinte código:

```
public interface IMediator{void SendMessage(Colleague caller, string msg);}
```

em seguida irei criar a classe abstrata Colleague, que irá conter o seguinte código:

```
public abstract class Colleague{protected IMediator _mediator;public Colleague(IMediator mediator){_mediator = mediator;}}
```

agora vou criar duas classes concretas que irão herdar de Colleague:

- ConcreteColleagueA, que irá conter o seguinte código:

```
public class ConcreteColleagueA : Colleague{public ConcreteColleagueA(IMediator mediator) : base(mediator) { }public void Send(string msg){Console.WriteLine("A send message:" + msg);_mediator.SendMessage(this, msg);}public void Receive(string msg){Console.WriteLine("A receive message:" + msg);}}
```

- ConcreteColleagueB, que irá conter o seguinte código:

```
public class ConcreteColleagueB : Colleague{public ConcreteColleagueB(IMediator mediator) : base(mediator) { }public void Send(string msg){Console.WriteLine("B send message:" + msg);_mediator.SendMessage(this, msg);}public void Receive(string msg){Console.WriteLine("B receive message:" + msg);}}
```

E por fim vou criar nosso ConcreteMediator que irá implementar nossa interface IMediator, e que irá conter o seguinte código:

```
public class ConcreteMediator : IMediator{public ConcreteColleagueA Colleague1 { get; set; }public ConcreteColleagueB Colleague2 { get; set; }public void SendMessage(Colleague caller, string msg){if (caller == Colleague1)Colleague2.Receive(msg);elseColleague1.Receive(msg);}}
```

E por fim irei alterar nossa classe Program.cs para que seja possível testar nosso Mediator, e ela irá conter o seguinte código:

```
class Program{static void Main(string[] args){ConcreteMediator mediator = new ConcreteMediator();mediator.Colleague1 = new ConcreteColleagueA(mediator);mediator.Colleague2 = new ConcreteColleagueB(mediator);mediator.SendMessage(mediator.Colleague1, "Message mediator 1");mediator.SendMessage(mediator.Colleague2, "Message mediator 2");Console.WriteLine("Press any key to continue!");Console.ReadKey();}}
```

Bom pessoal, espero que o exemplo fique claro e que vocês consigam levar esse exemplo para o mundo real, tirando strategy, mediator é meu padrão favorito, e ele acabou me ajudando algumas vezes. Vou ficando por aqui até a próxima pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsXpXp Inc

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