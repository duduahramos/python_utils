---
title: "https://medium.com/xp-inc/design-patterns-parte-22-state-73c5cda90029"
source_url: "https://medium.com/xp-inc/design-patterns-parte-22-state-73c5cda90029"
---
# Design Patterns - Parte 22 -State

Jones Roberto Nuzzi4 min read·Feb 19, 2020

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite que um objeto altere seu comportamento quando seu estado interno for alterado. Parece que o objeto mudou de classe.

# Problema

O padrão de estado está intimamente relacionado ao conceito de uma máquina de estado finito.

A idéia principal é que, a qualquer momento, existe um número finito de estados nos quais um programa pode estar. Dentro de qualquer estado único, o programa se comporta de maneira diferente e o programa pode ser alternado de um estado para outro instantaneamente. No entanto, dependendo do estado atual, o programa pode ou não mudar para outros estados. Essas regras de comutação, chamadas transições , também são finitas e predeterminadas.

# Solução

O padrão State sugere que você crie novas classes para todos os estados possíveis de um objeto e extraia todos os comportamentos específicos do estado para essas classes.

Em vez de implementar todos os comportamentos por conta própria, o objeto original, chamado contexto , armazena uma referência a um dos objetos de estado que representam seu estado atual e delega todo o trabalho relacionado a esse objeto.

Para fazer a transição do contexto para outro estado, substitua o objeto de estado ativo por outro objeto que represente esse novo estado. Isso é possível apenas se todas as classes de estado seguirem a mesma interface e o próprio contexto trabalhar com esses objetos por meio dessa interface.

# Implementação

O diagrama de classes UML para a implementação do State Design Pattern é fornecido abaixo:

<!-- image -->

# Prós

- Princípio de responsabilidade única . Organize o código relacionado a estados específicos em classes separadas.
- Princípio Aberto / Fechado . Introduzir novos estados sem alterar as classes de estado existentes ou o contexto.
- Simplifique o código do contexto, eliminando condicionais volumosos da máquina de estado.

# Contras

- A aplicação do padrão pode ser um exagero se uma máquina de estados tiver apenas alguns estados ou raramente mudar.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Context

Esta é uma classe que contém um objeto de estado concreto que fornece o comportamento de acordo com seu estado atual. Isso é usado pelos clientes.

## State

Essa é uma interface usada pelo objeto Context para acessar a funcionalidade alterável.

## ConcreteStateA / B

Essas são classes que implementam a interface State e fornecem a funcionalidade real que será usada pelo objeto Context. Cada classe de estado concreto fornece comportamento aplicável a um único estado do objeto Context.

## Exemplo prático

Bom vamos ao exemplo, primeiro irei criar a classe Context, que irá conter o seguinte código:

```
class Context{private State _state = null;public Context(State state){this.TransitionTo(state);}public void TransitionTo(State state){Console.WriteLine($"Context: Transition to {state.GetType().Name}.");this._state = state;this._state.SetContext(this);}public void Request1(){this._state.Handle1();}public void Request2(){this._state.Handle2();}}
```

em seguida irei criar a classe abstrata State, que irá conter o seguinte código:

```
abstract class State{protected Context _context;public void SetContext(Context context){this._context = context;}public abstract void Handle1();public abstract void Handle2();}
```

na sequência irei criar as as classes ConcreteState, que irão herda de State,

- ConcreteStateA, que irá conter o seguinte código:

```
class ConcreteStateA : State{public override void Handle1(){Console.WriteLine("ConcreteStateA handles request1.");Console.WriteLine("ConcreteStateA wants to change the state of the context.");this._context.TransitionTo(new ConcreteStateB());}public override void Handle2(){Console.WriteLine("ConcreteStateA handles request2.");}}
```

- ConcreteStateB, que irá conter o seguinte código:

```
class ConcreteStateB : State{public override void Handle1(){Console.Write("ConcreteStateB handles request1.");}public override void Handle2(){Console.WriteLine("ConcreteStateB handles request2.");Console.WriteLine("ConcreteStateB wants to change the state of the context.");this._context.TransitionTo(new ConcreteStateA());}}
```

E por fim iremos alterar nossa classe Program.cs pra que seja possível executar nosso exemplo, e ela irá conter o seguinte código:

```
class Program{static void Main(string[] args){var context = new Context(new ConcreteStateA());context.Request1();context.Request2();}}
```

Bom vou ficando por aqui pessoal, lembrem que todos os exemplos estão no meu Github e podem ser baixados. Abraço, até mais.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design Patterns

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