---
title: "https://medium.com/xp-inc/desing-patterns-factory-method-a7496ae071aa"
source_url: "https://medium.com/xp-inc/desing-patterns-factory-method-a7496ae071aa"
---
# Design Patterns - Parte 3 - Factory Method

Jones Roberto Nuzzi4 min read·Oct 8, 2019

--

Share

<!-- image -->

# Intenção

Factory Method é um padrão de design criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objeto que será criado.

# Problema

Imagine que você está criando um aplicativo de gerenciamento de logística. A primeira versão do seu aplicativo o único transporte utilizado é o de caminhões, portanto a maior parte do seu código fica dentro da classe Truck.

Depois de um tempo, sua empresa cresce muito e se torna bastante popular. Então agora você precisa adicionar o transporte marítimo no aplicativo.

Boas notícias para empresa, certo? Mas e o código? No momento, a maior parte do seu código é acoplada à classe Truck. A adição Ship ao aplicativo exigiria alterações em toda a base de código. Além disso, se mais tarde você decidir adicionar outro tipo de transporte ao aplicativo, provavelmente precisará fazer todas essas alterações novamente.

Como resultado, você terá um código bastante acoplado, repleto de condicionais que alteram o comportamento do aplicativo, dependendo da classe de objetos de transporte.

# Solução

O padrão Factory Method sugere que você substitua chamadas diretas de construção de objetos (usando o operador new) por chamadas para sua Factory Method. Objetos retornados por um Factory Method geralmente são chamados de "products".

À primeira vista, essa mudança pode parecer inútil: acabamos de mover a chamada do construtor de uma parte do programa para outra. No entanto, considere o seguinte: agora você pode substituir o Factory Method em uma subclasse e alterar a classe de produtos que estão sendo criados pelo método.

Porém, há uma pequena limitação: as subclasses podem retornar tipos diferentes de produtos somente se esses produtos tiverem uma classe ou interface básica comum. Além disso, o Factory Method na classe base deve ter seu tipo de retorno declarado como essa interface.

# Implementação

O diagrama de classes UML para a implementação do padrão de design do FactoryMethod é apresentado abaixo:

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Product

Esta é uma interface para criar os objetos.

## ConcreteProduct

Esta é uma classe que implementa a interface do produto.

## Creator

Esta é uma classe abstrata e declara o método factory, que retorna um objeto do tipo Product.

## ConcreteCreator

Esta é uma classe que implementa a classe Creator e substitui o método factory para retornar uma instância de um ConcreteProduct.

# Prós

- Você evita um acoplamento rígido entre o criador e os produtos de concreto.
- Princípio de responsabilidade única (single responsability) . Você pode mover o código de criação do produto para um local do programa, facilitando o suporte ao código.
- Princípio Open/Closed . Você pode introduzir novos tipos de produtos no programa sem quebrar o código do cliente existente.

# Contras

- O código pode se tornar mais complicado, pois você precisa introduzir muitas subclasses novas para implementar o padrão. O melhor cenário é quando você está introduzindo o padrão em uma hierarquia existente de classes de criadores.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

As classes, interfaces e objetos no diagrama de classes acima podem ser identificados da seguinte maneira:

IFactory - Interface

Scooter e Bike - ConcreateProduct

VehicleFactory - Creator

ConcreteVehicleFactory - Concreate Creator

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos ao exemplo prático. Primeiro iremos criar a interface IFactory, ela terá o seguinte código:

```
public interface IFactory{void Drive(int miles);}
```

Em seguida irei adicionar as classes Scooter e Bike elas irão implementar IFactory, com o seguinte código:

```
public class Bike : IFactory{public void Drive(int miles){Console.WriteLine($"Drive the Bike : {miles} km");}}
```

```
public class Scooter : IFactory{public void Drive(int miles){Console.WriteLine($"Drive the Scooter : {miles} km");}}
```

Em seguida iremos adicionar a classe abstrata Creator ela irá se chamar VehicleFactory, e irá conter o seguinte código:

```
public abstract class VehicleFactory{public abstract IFactory GetVehicle(string vehicle);}
```

Agora iremos criar a classe que irá herdar de VehicletFactory, ela será nossa classe concreta e será chamada ConcreteVehicleFactory, e terá o seguinte código:

```
public class ConcreteVehicleFactory : VehicleFactory{public override IFactory GetVehicle(string Vehicle){switch (Vehicle){case "Scooter":return new Scooter();case "Bike":return new Bike();default:throw new ApplicationException($"Vehicle {Vehicle} cannot be created");}}}
```

Agora falta somente a nossa classe Program do nosso console, e iremos ajustar o código para ficar assim:

```
class Program{static void Main(string[] args){VehicleFactory factory = new ConcreteVehicleFactory();IFactory scooter = factory.GetVehicle("Scooter");scooter.Drive(10);IFactory bike = factory.GetVehicle("Bike");bike.Drive(20);Console.ReadKey();}}
```

Lembrando que todos os exemplos podem ser baixados do meu github:

Bom vou ficando por aqui, qualquer dúvida podem entra em contato.

Abraço pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsXp IncXp LabsXp Investimentos

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