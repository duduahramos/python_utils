---
title: "https://medium.com/xp-inc/design-patterns-abstract-factory-da6b7057abce"
source_url: "https://medium.com/xp-inc/design-patterns-abstract-factory-da6b7057abce"
---
# Design Patterns - Parte 4 - Abstract Factory

Jones Roberto Nuzzi5 min read·Oct 9, 2019

--

Share

<!-- image -->

# Intenção

Abstract Factory é um padrão de design criacional que permite produzir famílias de objetos relacionados sem especificar suas classes concretas.A ideia principal é:

- Fornecer uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
- Uma hierarquia que encapsula: muitas "plataformas" possíveis e a construção de um conjunto de "produtos".

# Problema

Imagine que você está criando um simulador de loja de móveis. Seu código consiste em classes que representam:

1. Uma família de produtos relacionados, digamos: Chair+ Sofa+ CoffeeTable.
2. Várias variantes desta família. Por exemplo, produtos Chair+ Sofa+ CoffeeTableestão disponíveis nestas variantes: Modern, Victorian, ArtDeco.

Famílias de produtos e suas variantes.

<!-- image -->

Você precisa de uma maneira de criar objetos de móveis individuais para que eles correspondam a outros objetos da mesma família. Os clientes ficam muito bravos quando recebem móveis que não combinam.

Esse padrão é encontrado no equipamento de estampagem de chapa usado na fabricação de automóveis japoneses.

Além disso, você não deseja alterar o código existente ao adicionar novos produtos ou famílias de produtos ao programa. Os fornecedores de móveis atualizam seus catálogos com muita frequência e você não deseja alterar o código principal toda vez que isso acontece.

# Solução

Forneça um nível de indireção que abstraia a criação de famílias de objetos relacionados ou dependentes sem especificar diretamente suas classes concretas. O objeto "factory" tem a responsabilidade de fornecer serviços de criação para toda a família. Os clientes nunca criam objetos diretamente, eles pedem à fábrica que faça isso por eles.

Esse mecanismo facilita a troca de produtos entre famílias, porque a classe específica do objeto factory aparece apenas uma vez no aplicativo - onde é instanciada. O aplicativo pode substituir de uma vez toda a família de produtos simplesmente instanciando uma instância concreta diferente da AbstractFactory.

Como o serviço fornecido pela factory é muito difundido, ele é implementado normalmente utilizando Singleton.

# Implementação

<!-- image -->

## AbstractFactory

Esta é uma interface usada para criar produtos abstratos

## ConcreteFactory

Esta é uma classe que implementa a interface AbstractFactory para criar produtos concretos.

## AbstractProduct

Esta é uma interface que declara um tipo de produto.

## ConcreteProduct

Esta é uma classe que implementa a interface AbstractProduct para criar um produto

## Client

Esta é uma classe que usa as interfaces AbstractFactory e AbstractProduct para criar uma família de objetos relacionados.

# Prós

- Você pode ter certeza de que os produtos que você obtém de uma Factory são compatíveis entre si.
- Você evita acoplamentos rígidos entre produtos e o código client.
- Princípio de responsabilidade única. Você pode extrair o código de criação do produto em um único local, facilitando o suporte ao código.
- Princípio Open/Closed . Você pode introduzir novas variantes de produtos sem quebrar o código client existente.

# Contras

- O código pode se tornar mais complicado do que deveria ser, pois muitas novas interfaces e classes são introduzidas junto com o padrão.
- Ao adicionar ou remover produtos é necessária a modificação da AbstractFactory, gerando um grande trabalho, pois deve-se modificar todas as implementações da Factory e o client que usa a AbstractFactory.

# Exemplo

## O que é o que?

As classes, interfaces e objetos no diagrama de classes podem ser identificados da seguinte maneira:

VehicleFactory - interface AbstractFactory

HondaFactory e SuzukiFactory- ConcreteFactory

Bike , Scooter e Car- AbstractProduct

RegularBike, SportsBike, RegularScooter, Scooty, RegularCar e SportsCar- ConcreteProduct

VehicleClient - Client

## Diagrama de classes:

<!-- image -->

## Exemplo prático

Vamos começar criando a interface VehicleFactory, elá irá conter o seguinte código:

```
public interface VehicleFactory{Bike GetBike(string bike);Scooter GetScooter(string scooter);Car GetCar(string car);}
```

Em seguida iremos adicionar as classes HondaFactory e SuzukiFactory:

```
class HondaFactory : VehicleFactory{public Bike GetBike(string bike){switch (bike){case "Sports":return new SportsBike();case "Regular":return new RegularBike();default:throw new ApplicationException(string.Format("Vehicle '{0}' cannot be created", bike));}}public Car GetCar(string car){switch (car){case "Sports":return new SportsCar();case "Regular":return new RegularCar();default:throw new ApplicationException(string.Format("Vehicle '{0}' cannot be created", car));}}public Scooter GetScooter(string scooter){switch (scooter){case "Sports":return new Scooty();case "Regular":return new RegularScooter();default:throw new ApplicationException(string.Format("Vehicle '{0}' cannot be created", scooter));}}}
```

```
class SuzukiFactory : VehicleFactory{public Bike GetBike(string bike){switch (bike){case "Sports":return new SportsBike();case "Regular":return new RegularBike();default:throw new ApplicationException(string.Format("Vehicle '{0}' cannot be created", bike));}}public Car GetCar(string car){switch (car){case "Sports":return new SportsCar();case "Regular":return new RegularCar();default:throw new ApplicationException(string.Format("Vehicle '{0}' cannot be created", car));}}public Scooter GetScooter(string scooter){switch (scooter){case "Sports":return new Scooty();case "Regular":return new RegularScooter();default:throw new ApplicationException(string.Format("Vehicle '{0}' cannot be created", scooter));}}}
```

na sequência irei adicionar as interfaces dos produtos Bike,Scooter e Car:

```
public interface Bike{string Name();}public interface Car{string Name();}public interface Scooter{string Name();}
```

Adicionei em apenas um bloco para simplificar a postagem, no exemplo do Github as interfaces são arquivos sepa

na sequência irei adicionar as classes que implementam os AbstractProduct, elas são as classes ConcreteProduct

```
public class RegularBike : Bike{public string Name(){return "Regular Bike- Name";}}public class RegularCar : Car{public string Name(){return "Regular Car- Name";}}public class RegularScooter : Scooter{public string Name(){return "Regular Scooter- Name";}}public class Scooty : Scooter{public string Name(){return "Scooty- Name";}}public class SportsCar : Car{public string Name(){return "Sports Car - Name";}}
```

Na sequência irei criar a classe VehicleClient, com o seguinte código:

```
public class VehicleClient{Bike bike;Scooter scooter;Car car;public VehicleClient(VehicleFactory factory, string type){bike = factory.GetBike(type);scooter = factory.GetScooter(type);car = factory.GetCar(type);}public string GetBikeName(){return bike.Name();}public string GetScooterName(){return scooter.Name();}public string GetCar(){return car.Name();}}
```

e por último irei ajustar meu console para testar o nosso design, ele terá o seguinte código:

```
class Program{static void Main(string[] args){VehicleFactory honda = new HondaFactory();VehicleClient hondaclient = new VehicleClient(honda, "Regular");Console.WriteLine("******* Honda **********");Console.WriteLine(hondaclient.GetBikeName());Console.WriteLine(hondaclient.GetScooterName());hondaclient = new VehicleClient(honda, "Sports");Console.WriteLine(hondaclient.GetBikeName());Console.WriteLine(hondaclient.GetScooterName());hondaclient = new VehicleClient(honda, "Regular");Console.WriteLine(hondaclient.GetCar());VehicleFactory suzuki = new SuzukiFactory();VehicleClient suzukiClient = new VehicleClient(suzuki, "Regular");Console.WriteLine("******* Suzuki **********");Console.WriteLine(suzukiClient.GetBikeName());Console.WriteLine(suzukiClient.GetScooterName());suzukiClient = new VehicleClient(suzuki, "Sports");Console.WriteLine(suzukiClient.GetBikeName());Console.WriteLine(suzukiClient.GetScooterName());suzukiClient = new VehicleClient(honda, "Regular");Console.WriteLine(suzukiClient.GetCar());Console.ReadKey();}}
```

Lembrando que todos os exemplos da série de patterns podem ser baixados do meu GitHub, bom até a próxima pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsXp IncXp InvestimentosDevelopmentDeveloper

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