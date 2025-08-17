---
title: "https://medium.com/xp-inc/desing-patterns-parte-11-decorator-ba348f44142f"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-11-decorator-ba348f44142f"
---
# Design Patterns - Parte 11 - Decorator

Jones Roberto Nuzzi5 min read·Nov 20, 2019

--

Share

<!-- image -->

# Intenção

O Decorator é um padrão de design estrutural que permite anexar novos comportamentos aos objetos, colocando-os dentro de objetos especiais do wrapper que contêm os comportamentos.

# Problema

Você deseja adicionar comportamento ou estado a objetos individuais em tempo de execução. A herança não é viável porque é estática e se aplica a uma classe inteira.

# Solução

Estender uma classe é a primeira coisa que vem à mente quando você precisa alterar o comportamento de um objeto. No entanto, a herança tem várias advertências sérias que você precisa estar ciente.

- A herança é estática. Você não pode alterar o comportamento de um objeto existente no tempo de execução. Você só pode substituir o objeto inteiro por outro criado a partir de uma subclasse diferente.
- As subclasses podem ter apenas uma classe pai. Na maioria dos idiomas, a herança não permite que uma classe herde comportamentos de várias classes ao mesmo tempo.

Uma das maneiras de superar essas advertências é usando Agregação ou Composição em vez de herança . Ambas as alternativas funcionam quase da mesma maneira: um objeto fazreferência a outro e delega-lhe algum trabalho, enquanto que com a herança, o próprio objeto é capaz de fazer esse trabalho, herdando o comportamento de sua superclasse.

Com essa nova abordagem, você pode facilmente substituir o objeto "auxiliar" vinculado por outro, alterando o comportamento do contêiner em tempo de execução. Um objeto pode usar o comportamento de várias classes, tendo referências a vários objetos e delegando a eles todos os tipos de trabalho. A agregação / composição é o princípio principal por trás de muitos padrões de design, incluindo o Decorator. Nessa nota, vamos voltar à discussão sobre padrões.

# Implementação

O diagrama de classes UML para a implementação do padrão de design do decorador é apresentado abaixo:

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Component

Essa é uma interface que contém membros que serão implementados pela ConcreteClass e Decorator.

## ConcreteComponent

Esta é uma classe que implementa a interface do componente.

## Decorator

Esta é uma classe abstrata que implementa a interface Component e contém a referência a uma instância Component. Essa classe também atua como classe base para todos os decoradores de componentes.

## ConcreteDecorator

Esta é uma classe que herda da classe Decorator e fornece um decorador para componentes.

# Prós

- Você pode estender o comportamento de um objeto sem criar uma nova subclasse.
- Você pode adicionar ou remover responsabilidades de um objeto em tempo de execução.
- Você pode combinar vários comportamentos envolvendo um objeto em vários decoradores.
- Princípio de responsabilidade única . Você pode dividir uma classe monolítica que implementa muitas variantes possíveis de comportamento em várias classes menores.

# Contras

- É difícil remover um invólucro específico da pilha de invólucros.
- É difícil implementar um decorador de forma que seu comportamento não dependa da ordem na pilha de decoradores.
- O código de configuração inicial das camadas pode parecer bastante feio.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

As classes, interfaces e objetos no diagrama de classes acima podem ser identificados da seguinte maneira:

Vehicle - Interface Component .

HondaCity- classe ConcreteComponent .

VehicleDecorator- classe Decorator.

SpecialOffer - classe ConcreteDecorator.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos lá, irei começar adicionando nosso 'Component' , vou começar adicionando a interface IVehicle, que irá conter os atributos do nosso component. a interface irá conter o código a seguir:

```
public interface IVehicle{string Make { get; }string Model { get; }double Price { get; }}
```

em seguida iremos adicionar nossa classe que será nosso 'ConcreteComponent', irei colocar o nome HondaCity, e ela irá conter o seguinte código:

```
public class HondaCity : IVehicle{public string Make{get { return "HondaCity"; }}public string Model{get { return "CNG"; }}public double Price{get { return 1000000; }}}
```

em seguida irei adicionar o nosso 'Decorator', essa classe terá o nome de VehicleDecorator, e ela irá implementar IVehicle

```
public abstract class VehicleDecorator : IVehicle{private IVehicle _vehicle;public VehicleDecorator(IVehicle vehicle){_vehicle = vehicle;}public string Make{get { return _vehicle.Make; }}public string Model{get { return _vehicle.Model; }}public double Price{get { return _vehicle.Price; }}}
```

e agora irei adicionar a classe promocional que também é um ConcreteComponent porém ela implementa nosso 'Decorator' VehicleDecorator, o nome dela será SpecialOffer, e irá conter o seguinte código:

```
public class SpecialOffer : VehicleDecorator{public SpecialOffer(IVehicle vehicle) : base(vehicle) { }public int DiscountPercentage { get; set; }public string Offer { get; set; }public double Price{get{double price = base.Price;int percentage = 100 - DiscountPercentage;return Math.Round((price * percentage) / 100, 2);}}}
```

E por último irei adaptar nossa classe Program.cs para que nosso console execute o padrão Decorator, o código ficar assim:

```
class Program{static void Main(string[] args){HondaCity car = new HondaCity();Console.WriteLine($"Honda City preço : {car.Price}");SpecialOffer offer = new SpecialOffer(car);offer.DiscountPercentage = 25;offer.Offer = "25 % de desconto";Console.WriteLine($"{offer.Price} @ Honda preço especial : {offer.Offer} ");Console.ReadKey();}}
```

Lembrando que é possivel baixar o código fonte de exemplo direto no meu github, os links estão no final da página, até a próxima pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Xp IncXp InvestimentosCsharpDesign Patterns

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