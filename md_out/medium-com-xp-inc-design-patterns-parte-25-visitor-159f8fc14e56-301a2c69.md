---
title: "https://medium.com/xp-inc/design-patterns-parte-25-visitor-159f8fc14e56"
source_url: "https://medium.com/xp-inc/design-patterns-parte-25-visitor-159f8fc14e56"
---
# Design Patterns - Parte 25 - Visitor

Jones Roberto Nuzzi4 min read·Mar 12, 2020

--

1

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite separar algoritmos dos objetos nos quais eles operam.

# Problema

Muitas operações distintas e não relacionadas precisam ser executadas em objetos de nó em uma estrutura agregada heterogênea. Você deseja evitar "poluir" as classes de nós com essas operações. E não é necessário consultar o tipo de cada nó e converter o ponteiro no tipo correto antes de executar a operação desejada.

# Solução

O padrão Visitor sugere que você coloque o novo comportamento em uma classe separada chamada visitor , em vez de tentar integrá-lo às classes existentes. O objeto original que tinha que executar o comportamento agora é passado para um dos métodos do visitante como argumento, fornecendo ao método acesso a todos os dados necessários contidos no objeto.

# Implementação

O diagrama de classes UML para a implementação do Visitor Design Pattern é fornecido abaixo:

<!-- image -->

# Prós

- Princípio Aberto / Fechado . Você pode introduzir um novo comportamento que possa trabalhar com objetos de diferentes classes sem alterar essas classes.
- Princípio de responsabilidade única . Você pode mover várias versões do mesmo comportamento para a mesma classe.
- Um objeto visitante pode acumular algumas informações úteis ao trabalhar com vários objetos. Isso pode ser útil quando você deseja percorrer alguma estrutura complexa de objetos, como uma árvore de objetos, e aplicar o visitante a cada objeto dessa estrutura.

# Contras

- Você precisa atualizar todos os visitantes cada vez que uma classe é adicionada ou removida da hierarquia de elementos.
- Os visitantes podem não ter acesso necessário aos campos e métodos particulares dos elementos com os quais devem trabalhar.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Client

Esta é uma classe que tem acesso aos objetos da estrutura de dados e pode instruí-los a aceitar um Visitante para executar as operações apropriadas.

## ObjectStructure

Esta é uma classe que contém todos os elementos que podem ser usados pelos visitantes.

## Element

Essa é uma interface que especifica a operação Accept.

## ConcreteElement

Essas são classes que implementam a interface Element e mantêm as informações reais.

## Visitor

Essa é uma interface que especifica as operações de Visita para visitantes concretos.

## ConcreteVisitor

Essas são subclasses que implementam a interface do visitante.

## Exemplo prático

Bom vamos para o nosso exemplo prático, vou começar criando a interface IElement, que irá conter o seguinte código:

```
public interface IElement{void Accept(IVisitor visitor);}
```

Em seguida irei criar duas classes concretas que irão implementar nosso IElement

- ConcreteElementA

```
public class ConcreteElementA : IElement{public void Accept(IVisitor visitor){visitor.VisitConcreteElementA(this);}public string ExclusiveMethodOfConcreteElementA(){return "A";}}
```

- ConcreteElementB

```
public class ConcreteElementB : IElement{public void Accept(IVisitor visitor){visitor.VisitConcreteElementB(this);}public string SpecialMethodOfConcreteElementB(){return "B";}}
```

Em seguida iremos criar uma interface IVisitor, que irá conter o seguinte código:

```
public interface IVisitor{void VisitConcreteElementA(ConcreteElementA element);void VisitConcreteElementB(ConcreteElementB element);}
```

Em seguida iremos criar nossas classes concretas que implementam a interface IVisitor

- ConcreteVisitor1

```
class ConcreteVisitor1 : IVisitor{public void VisitConcreteElementA(ConcreteElementA element){Console.WriteLine($"{element.ExclusiveMethodOfConcreteElementA()} ConcreteVisitor1");}public void VisitConcreteElementB(ConcreteElementB element){Console.WriteLine($"{element.SpecialMethodOfConcreteElementB()} ConcreteVisitor1");}}
```

- ConcreteVisitor2

```
class ConcreteVisitor2 : IVisitor{public void VisitConcreteElementA(ConcreteElementA element){Console.WriteLine($"{element.ExclusiveMethodOfConcreteElementA()} ConcreteVisitor2");}public void VisitConcreteElementB(ConcreteElementB element){Console.WriteLine($"{element.SpecialMethodOfConcreteElementB()} ConcreteVisitor2");}}
```

Em seguida iremos criar nossa classe Client, que irá conter o seguinte código:

e por fim vamos alterar nossa classe Program.cs, que será nossa ObjectStructure, que irá conter o seguinte código:

```
class Program{static void Main(string[] args){List<IElement> components = new List<IElement>{new ConcreteElementA(),new ConcreteElementB()};Console.WriteLine("The client code works with all visitors via the base Visitor interface:");var visitor1 = new ConcreteVisitor1();Client.ClientCode(components, visitor1);Console.WriteLine();Console.WriteLine("It allows the same client code to work with different types of visitors:");var visitor2 = new ConcreteVisitor2();Client.ClientCode(components, visitor2);Console.WriteLine("Press any key to continue!");Console.ReadKey();}}
```

Bom pessoal, esse é nosso último artigo sobre design patterns do GOF, em breve irei começar a falar de design patterns que estou usando nas novas arquiteturas para nuvem, e também pretendo falar sobre os padrões do GRASP, espero que tenham gostado da série, que no total foi de 25 artigos.

Lembrando que todo o código está em meu github se tiver qualquer dúvida pode comentar, que eu irei tentar responder. Abraços e até mais.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design Patterns

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