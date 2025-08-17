---
title: "https://medium.com/xp-inc/desing-patterns-parte-12-facade-ff66c68f5784"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-12-facade-ff66c68f5784"
---
# Intenção

Facade é um padrão de design estrutural que fornece uma interface simplificada para uma biblioteca, uma estrutura ou qualquer outro conjunto complexo de classes. Quando falamos de design patterns facade é um dos mais conhecidos, assim como singleton.

# Problema

Imagine que você deve fazer seu código funcionar com um amplo conjunto de objetos que pertencem a uma biblioteca ou estrutura sofisticada. Normalmente, você precisa inicializar todos esses objetos, acompanhar as dependências, executar métodos na ordem correta e assim por diante.

Como resultado, a lógica comercial de suas classes ficaria fortemente acoplada aos detalhes de implementação de classes de terceiros, dificultando a compreensão e a manutenção.

# Solução

Facade discute o encapsulamento de um subsistema complexo em um único objeto de interface. Isso reduz a curva de aprendizado necessária para alavancar com sucesso o subsistema. Também promove a dissociação do subsistema de seus muitos clientes potencialmente. Por outro lado, se a Facade for o único ponto de acesso para o subsistema, limitará os recursos e a flexibilidade que "usuários avançados" podem precisar.

O objeto Fachada deve ser um advogado ou facilitador bastante simples. Não deve se tornar um oráculo onisciente ou um objeto "deus".

# Implementação

O diagrama de classes UML para a implementação do padrão de design de fachada é apresentado abaixo:

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Complex System

Uma biblioteca de subsistemas.

## SubsystemA, SubsystemB, SubsystemC

Essas são classes dentro de um sistema complexo e oferecem operações detalhadas.

## Facade

Esta é uma classe de wrapper cuja classe de wrapper contém um conjunto de membros exigidos pelo cliente.

## Client

Esta é uma classe que chama as operações de alto nível na fachada.

# Prós

Você pode isolar seu código da complexidade de um subsistema.

# Contras

Uma fachada pode se tornar um objeto deus associado a todas as classes de um aplicativo.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

As classes, interfaces e objetos no diagrama de classes acima podem ser identificados da seguinte maneira:

CarModel, CarEngine, CarBody, CarAccessories - são subsystems.

CarFacade- classe Facade

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos tentar exemplificar da maneira mais simples possível a implementação de uma Facade. vamos começar pela classe CarModel, que irá conter o seguinte código:

```
class CarModel{public void SetModel(){Console.WriteLine(" CarModel - SetModel");}}
```

em seguida irei adicionar mais uma classe Subsystem essa por sua vez irá se chamar CarEngine, e irá conter o seguinte código:

```
class CarEngine{public void SetEngine(){Console.WriteLine(" CarEngine - SetEngine");}}
```

e agora iremos adicionar o outro Subsystem que terá o nome de CarBody, com o seguinte código:

```
class CarBody{public void SetBody(){Console.WriteLine(" CarBody - SetBody");}}
```

e agora iremos adicionar nosso ultimo Subsystem do exemplo, que irá se chamar CarAccessories, e terá o seguinte código:

```
class CarAccessories{public void SetAccessories(){Console.WriteLine(" CarAccessories - SetAccessories");}}
```

Agora iremos adicionar a classe que será nossa Facade, ela se chamará CarFacade, e terá o seguinte código:

```
public class CarFacade{CarModel model;CarEngine engine;CarBody body;CarAccessories accessories;public CarFacade(){model = new CarModel();engine = new CarEngine();body = new CarBody();accessories = new CarAccessories();}public void CreateCompleteCar(){Console.WriteLine("******** Creating a Car **********\n");model.SetModel();engine.SetEngine();body.SetBody();accessories.SetAccessories();Console.WriteLine("\n******** Car creation complete **********");}}
```

e agora por último iremos modificar nossa classe de console, para conseguirmos testar o nosso exemplo, ela ficará com o seguinte código:

```
class Program{static void Main(string[] args){CarFacade facade = new CarFacade();facade.CreateCompleteCar();Console.ReadKey();}}
```

Bom pessoal, tentei ser o mais sucinto possível, vou ficando por aqui, não deixe de acompanhar a postagem da semana que vem irei falar do próximo pattern da lista, que será o Flyweight.

Não esqueça que os exemplos estão no Github. Abraço, até mais pessoal.

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