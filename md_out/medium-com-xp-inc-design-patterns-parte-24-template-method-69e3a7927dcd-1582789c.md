---
title: "https://medium.com/xp-inc/design-patterns-parte-24-template-method-69e3a7927dcd"
source_url: "https://medium.com/xp-inc/design-patterns-parte-24-template-method-69e3a7927dcd"
---
# Design Patterns - Parte 24 -Template Method

Jones Roberto Nuzzi3 min read·Mar 10, 2020

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que define o esqueleto de um algoritmo na superclasse, mas permite que as subclasses substituam etapas específicas do algoritmo sem alterar sua estrutura.

# Problema

Dois componentes diferentes têm semelhanças significativas, mas não demonstram reutilização de interface ou implementação comum. Se uma alteração comum a ambos os componentes for necessária, um esforço duplicado deverá ser gasto.

# Solução

O padrão do Template Method sugere que você divida um algoritmo em uma série de etapas, transforme essas etapas em métodos e faça uma série de chamadas para esses métodos em um único "template method". As etapas podem ser abstract ou ter algum padrão implementação. Para usar o algoritmo, o cliente deve fornecer sua própria subclasse, implementar todas as etapas abstratas e substituir algumas opcionais, se necessário (mas não o próprio método de modelo).

# Implementação

O diagrama de classes UML para a implementação do Template Method Design Pattern é apresentado abaixo:

<!-- image -->

# Prós

- Você pode permitir que os clientes substituam apenas certas partes de um algoritmo grande, tornando-os menos afetados pelas alterações que acontecem com outras partes do algoritmo.
- Você pode colocar o código duplicado em uma superclasse.

# Contras

- Alguns clientes podem ser limitados pelo esqueleto fornecido de um algoritmo.
- Você pode violar o princípio de substituição de Liskov suprimindo uma implementação de etapa padrão por meio de uma subclasse.
- Os métodos de modelo tendem a ser mais difíceis de manter quanto mais etapas eles tiverem.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## AbstractClass

Esta é uma classe abstrata que contém o método de modelo e operações abstratas para cada uma das etapas que podem ser implementadas pelas subclasses.

## ConcreteClass

Essas são subclasses que herdam a classe abstrata e substituem as operações da classe abstrata.

## Exemplo prático

Bom vamos ao nosso exemplo prático, irei começar por nossa classe abstrata,e ela irá conter o seguinte código:

```
abstract class AbstractClass{public void TemplateMethod(){this.BaseOperation1();this.RequiredOperations1();this.BaseOperation2();this.Hook1();this.RequiredOperation2();this.BaseOperation3();this.Hook2();}protected void BaseOperation1(){Console.WriteLine("AbstractClass says: I am doing the bulk of the work");}protected void BaseOperation2(){Console.WriteLine("AbstractClass says: But I let subclasses override some operations");}protected void BaseOperation3(){Console.WriteLine("AbstractClass says: But I am doing the bulk of the work anyway");}protected abstract void RequiredOperations1();protected abstract void RequiredOperation2();protected virtual void Hook1() { }protected virtual void Hook2() { }}
```

em seguida irei criar duas classes concretas que herdam da nossa classe abstrata

- ConcreteClass1

```
class ConcreteClass1 : AbstractClass{protected override void RequiredOperations1(){Console.WriteLine("ConcreteClass1 says: Implemented Operation1");}protected override void RequiredOperation2(){Console.WriteLine("ConcreteClass1 says: Implemented Operation2");}}
```

- ConcreteClass2

```
class ConcreteClass2 : AbstractClass{protected override void RequiredOperations1(){Console.WriteLine("ConcreteClass2 says: Implemented Operation1");}protected override void RequiredOperation2(){Console.WriteLine("ConcreteClass2 says: Implemented Operation2");}protected override void Hook1(){Console.WriteLine("ConcreteClass2 says: Overridden Hook1");}}
```

Em seguida iremos criar nossa classe Client, ela irá receber nossa classe abstrata por paremetro no método ClientCode, e ela irá conter o seguinte código:

```
class Client{public static void ClientCode(AbstractClass abstractClass){abstractClass.TemplateMethod();}}
```

E por último iremos criar a classe Program.cs para conseguir testar nosso pattern, e ela irá conter o seguinte código:

```
static void Main(string[] args){Console.WriteLine("Same client code can work with different subclasses:");Client.ClientCode(new ConcreteClass1());Console.Write("\n");Console.WriteLine("Same client code can work with different subclasses:");Client.ClientCode(new ConcreteClass2());Console.WriteLine("Press any key to continue!");Console.ReadKey();}
```

Bom vou ficando por aqui pessoal, lembrando que todos os exemplos estão no meu github, e podem ser testados, é só baixar o código

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

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