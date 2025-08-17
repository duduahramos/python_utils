---
title: "https://medium.com/xp-inc/design-patterns-parte-13-flyweight-9f96433bce05"
source_url: "https://medium.com/xp-inc/design-patterns-parte-13-flyweight-9f96433bce05"
---
# Design Patterns - Parte 13 - Flyweight

Jones Roberto Nuzzi4 min read·Nov 28, 2019

--

Share

<!-- image -->

# Intenção

O Flyweight é um padrão de design estrutural que permite ajustar mais objetos à quantidade disponível de RAM, compartilhando partes comuns do estado entre vários objetos, em vez de manter todos os dados em cada objeto.

# Problema

Projetar objetos até os níveis mais baixos de "granularidade" do sistema fornece flexibilidade ideal, mas pode ser inaceitavelmente caro em termos de desempenho e uso de memória.

# Solução

O padrão Flyweight descreve como compartilhar objetos para permitir seu uso com granularidade fina sem custo proibitivo. Cada objeto "flyweight" é dividido em duas partes: a parte dependente do estado (extrínseca) e a parte independente do estado (intrínseca). O estado intrínseco é armazenado (compartilhado) no objeto Flyweight. O estado extrínseco é armazenado ou calculado pelos objetos do cliente e passado para o Flyweight quando suas operações são invocadas.

# Implementação

O diagrama de classes UML para a implementação do padrão de design flyweight é apresentado abaixo:

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Flyweight

Esta é uma interface que define os membros dos objetos flyweight.

## ConcreteFlyweight

Esta é uma classe que herda da classe Flyweight.

## UnsharedFlyweight

Esta é uma classe que Herda da classe Flyweight e permite o compartilhamento de informações,

é possível criar instâncias de classes concretas de flyweight que

não são compartilhadas.

## FlyweightFactory

Esta é uma classe que contém as referências de objetos flyweight já criados.

Quando o método GetFlyweight é chamado a partir do código do cliente, essas referências são verificadas para determinar se um objeto flyweight apropriado já está presente ou não. Se presente, é retornado.

Caso contrário, um novo objeto será gerado, adicionado à coleção e retornado.

# Prós

Você pode economizar muita memória RAM, assumindo que seu programa tenha vários objetos semelhantes.

# Contras

- Você pode negociar ciclos de RAM por CPU quando alguns dados de contexto precisarem ser recalculados toda vez que alguém chamar um método flyweight.
- O código se torna muito mais complicado. Os novos membros da equipe sempre se perguntarão por que o estado de uma entidade foi separado dessa maneira.

# Exemplo

## Uso do padrão em C#

<!-- image -->

## O que é oque?

As classes, interfaces e objetos no diagrama de classes acima podem ser identificados da seguinte maneira:

ShapeObjectFactory - classe FlyweightFactory.

IShape - interface Flyweight.

Circle &amp; Rectabgle - classe ConcreteFlyweight.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom esse é dos padrões mais chatos de entender, mas vou tentar criar um exemplo simples para absorver. Vamos começar pela interface IShape, que irá conter o seguinte código:

```
interface IShape{void Print();}
```

em seguida iremos criar a classe ConcreteFlyweight ela representará um Retângulo, que irá conter o seguinte código:

```
class Rectangle : IShape{public void Print(){Console.WriteLine("Printing Rectangle");}}
```

Adicionaremos também mais uma classe ConcreteFlyweight, ela representará um circulo, que irá conter o seguinte código:

```
class Circle : IShape{public void Print(){Console.WriteLine("Printing Circle");}}
```

A seguir adicionaremos a FlyweightFactory, quer será usada para criar os objetos que implementam IShape, ela irá conter o seguinte código:

```
class ShapeObjectFactory{Dictionary<string, IShape> shapes = new Dictionary<string, IShape>();public int TotalObjectsCreated{get { return shapes.Count; }}public IShape GetShape(string ShapeName){IShape shape = null;if (shapes.ContainsKey(ShapeName)){shape = shapes[ShapeName];}else{switch (ShapeName){case "Rectangle":shape = new Rectangle();shapes.Add("Rectangle", shape);break;case "Circle":shape = new Circle();shapes.Add("Circle", shape);break;default:throw new Exception("Factory cannot create the object specified");}}return shape;}}
```

Agora iremos modificar a classe Program, para que seja possivel realizarmos nossos testes, ela irá conter o seguinte código:

```
class Program{static void Main(string[] args){ShapeObjectFactory sof = new ShapeObjectFactory();IShape shape = sof.GetShape("Rectangle");shape.Print();shape = sof.GetShape("Rectangle");shape.Print();shape = sof.GetShape("Rectangle");shape.Print();shape = sof.GetShape("Circle");shape.Print();shape = sof.GetShape("Circle");shape.Print();shape = sof.GetShape("Circle");shape.Print();int NumObjs = sof.TotalObjectsCreated;Console.WriteLine("\nTotal No of Objects created = {0}", NumObjs);Console.ReadKey();}}
```

Espero que esse exemplo ajude a exemplificar o uso do Flyweight, que é um padrão pouco usado devido sua complexidade, lembrando sempre que o código fonte em C# encontra-se no github e pode ser baixado. Vou ficando por aqui, até a próxima pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Xp IncXp InvestimentosLab XpDesign Patterns

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