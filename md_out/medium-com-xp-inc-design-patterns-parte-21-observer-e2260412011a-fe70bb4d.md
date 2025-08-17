---
title: "https://medium.com/xp-inc/design-patterns-parte-21-observer-e2260412011a"
source_url: "https://medium.com/xp-inc/design-patterns-parte-21-observer-e2260412011a"
---
# Design Patterns - Parte 21 - Observer

Jones Roberto Nuzzi4 min read·Feb 4, 2020

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite definir um mecanismo de assinatura para notificar vários objetos sobre quaisquer eventos que ocorram no objeto que estão observando.

# Problema

Um grande projeto monolítico não se adapta bem à medida que novos requisitos de gráficos ou monitoramento são cobrados.

# Solução

Defina um objeto que seja o "guardião" do modelo de dados e / ou lógica de negócios (Subject). Delegue todas as funcionalidades de " view" a objetos Observer dissociados e distintos. Os observers se registram no Subject à medida que são criados. Sempre que o Subject muda, transmite a todos os Observers registrados que ele mudou, e cada Observer consulta o Subject pelo subconjunto do estado do Subject que é responsável pelo monitoramento.

Isso permite que o número e o "type" de objetos "view" sejam configurados dinamicamente, em vez de serem especificados estaticamente em tempo de compilação.

# Implementação

O diagrama de classes UML para a implementação do Observer Design Pattern é apresentado abaixo:

<!-- image -->

# Prós

- Princípio Aberto / Fechado . Você pode introduzir novas classes de assinantes sem precisar alterar o código do editor (e vice-versa, se houver uma interface do editor).
- Você pode estabelecer relações entre objetos em tempo de execução.

# Contras

- Os assinantes são notificados em ordem aleatória.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Subject

Esta é uma classe que contém uma coleção particular de observadores inscritos em um assunto para notificação usando a operação Notify.

## ConcreteSubject

Esta é uma classe que mantém seu próprio estado. Quando uma alteração é feita em seu estado, o objeto chama a operação Notify da classe base para indicar isso a todos os seus observadores.

## Observer

Essa é uma interface que define uma operação Update, que deve ser chamada quando o estado do sujeito mudar.

## ConcreteObserver

Esta é uma classe que implementa a interface do Observador e examina o assunto para determinar quais informações foram alteradas.

## Exemplo prático

Primeiro iremos criar uma interface IObserver que irá ser responsável por receber as atualizações do Subject, e irá conter o seguinte código:

```
publicinterfaceIObserver{voidUpdate(ISubject subject);}
```

Em seguida iremos criar a interface ISubject, ela será responsável pelo contrato de Subject, e irá conter o seguinte código:

```
publicinterfaceISubject{voidAttach(IObserver observer);voidDetach(IObserver observer);voidNotify();}
```

Em seguida iremos criar nosso Subject que irá implementar a interface ISubject, e irá conter o seguinte código:

```
public class Subject : ISubject{public int State { get; set; } = -0;private List<IObserver> _observers = new List<IObserver>();public void Attach(IObserver observer){Console.WriteLine("Subject: Attached an observer.");this._observers.Add(observer);}public void Detach(IObserver observer){this._observers.Remove(observer);Console.WriteLine("Subject: Detached an observer.");}public void Notify(){Console.WriteLine("Subject: Notifying observers...");foreach (var observer in _observers){observer.Update(this);}}public void SomeBusinessLogic(){Console.WriteLine("\nSubject: I'm doing something important.");this.State = new Random().Next(0, 10);Thread.Sleep(15);Console.WriteLine("Subject: My state has just changed to: " + this.State);this.Notify();}}
```

Agora iremos criar nossos ConcreteObservers, que irão implementer a interface IObserver e eles irão conter o seguinte código:

- ConcreteObserverA

```
class ConcreteObserverA : IObserver{public void Update(ISubject subject){if ((subject as Subject).State < 3){Console.WriteLine("ConcreteObserverA: Reacted to the event.");}}}
```

- ConcreteObserverB

```
class ConcreteObserverB : IObserver{public void Update(ISubject subject){if ((subject as Subject).State == 0 || (subject as Subject).State >= 2){Console.WriteLine("ConcreteObserverB: Reacted to the event.");}}}
```

E por fim iremos modificar nossa classe Program.cs para que seja possível executar nosso exemplo de Observer, e ele irá conter o seguinte código:

```
class Program{static void Main(string[] args){// The client code.var subject = new Subject();var observerA = new ConcreteObserverA();subject.Attach(observerA);var observerB = new ConcreteObserverB();subject.Attach(observerB);subject.SomeBusinessLogic();subject.SomeBusinessLogic();subject.Detach(observerB);subject.SomeBusinessLogic();}}
```

Bom vou ficando por aqui, e na semana que vem irei mostrar mais um exemplo dos padrões do GOF, até a próxima pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Desing PatternDesign PatternsXp Inc

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