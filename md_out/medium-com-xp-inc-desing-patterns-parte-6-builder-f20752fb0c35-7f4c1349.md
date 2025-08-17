---
title: "https://medium.com/xp-inc/desing-patterns-parte-6-builder-f20752fb0c35"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-6-builder-f20752fb0c35"
---
# Design Patterns - Parte 6 - Builder

Jones Roberto Nuzzi6 min read·Oct 30, 2019

--

Share

<!-- image -->

# Intenção

O Builder é um padrão de design criacional que permite construir objetos complexos passo a passo. O padrão permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção.

Além disso, o padrão builder descreve uma maneira de separar um objeto de sua construção. O mesmo método de construção pode criar uma representação diferente do objeto.

# Problema

<!-- image -->

Por exemplo, vamos pensar em como criar uma classe House. Para construir uma casa simples, você precisa construir quatro paredes e um piso, instalar portas, encaixar janelas e criar um telhado. Mas se você quiser uma casa maior de dois andares e com garagem para vários carros, com um quintal e outras coisas boas (como um sistema de aquecimento, encanamento e fiação elétrica)?

A solução mais simples é estender a class House e criar um conjunto de subclasses para cobrir todas as combinações dos parâmetros. Mas, eventualmente, você terminará com um número considerável de subclasses. Qualquer novo parâmetro, como o estilo de varanda, exigirá que a hierarquia cresça ainda mais.

Ou você também pode criar um construtor gigante na classe House com todos os parâmetros possíveis que controlam o objeto. Embora essa abordagem elimine a necessidade de subclasses, ela cria outro problema, vários parâmetros não serão utilizados, tornando o construtor grande e feio (e difícil de utilizar). Por exemplo, poucas casas tem piscinas; portanto, os parâmetros relacionados às piscinas seriam inúteis na maioria das vezes.

# Solução

O padrão Builder sugere que você extraia o código de construção do objeto de sua própria classe e o mova para objetos separados chamados builders.

<!-- image -->

O padrão Builder permite construir objetos complexos passo a passo. O Builder não permite que outros objetos acessem o produto enquanto ele está sendo construído.

O padrão organiza construção objeto organizando em um conjunto de passos. Para criar um objeto, você executa uma série dessas etapas em um objeto construtor. A parte importante é que você não precisa executar todas as etapas. Você pode chamar apenas as etapas necessárias para produzir uma configuração específica de um objeto.

Algumas das etapas de construção podem exigir implementação diferente quando você precisa criar várias representações do produto.

Nesse caso, você pode criar várias classes builders diferentes que implementam o mesmo conjunto de etapas de construção, mas de uma maneira diferente. Em seguida, você pode usar esses builders no processo de construção para produzir diferentes tipos de objetos.

# Implementação

<!-- image -->

## Product

A classe product define o tipo do objeto complexo que deve ser gerado pelo padrão do construtor.

## Builder

Esta classe abstrata que define todas as etapas que devem ser executadas para criar corretamente um produto. O método GetProduct é usado para devolver o produto final. A classe builder geralmente pode ser substituída por uma interface simples.

## ConcreteBuilder

Poderão haver várias classes de builder concretas herdadas do builder ou que implementam a interface builder (no caso de criar uma interface ao invés de classe abstrata). Essas classes contêm a funcionalidade para criar um produto complexo específico.

## Director

A classe director controla o algoritmo que gera o objeto do produto final. Um objeto director é instanciado e seu método Builder é chamado. O método inclui um parâmetro para capturar o objeto específico do ConcreteBuilder que deve ser usado para gerar o produto. O director chama os métodos do ConcreteBuilder na ordem correta para gerar o objeto do produto. Na conclusão do processo, o método GetProduct do objeto builder pode ser usado para retornar o produto final.

# Prós

- Você pode construir objetos passo a passo, adiar etapas de construção ou executar etapas recursivamente.
- Você pode reutilizar o mesmo código de construção ao criar várias representações de produtos.
- Princípio de responsabilidade única . Você pode isolar o código de construção complexo da lógica de negócios do produto.

# Contras

- A complexidade geral do código aumenta, pois o padrão requer a criação de várias novas classes.

# Exemplo

<!-- image -->

## O que é o que?

1. IVehicleBuilder - Builder interface
2. FerrariBuilder &amp; HondaBuilder- Concrete Builder
3. Vehicle- Product
4. Vehicle Creator - Director

## Diagrama de Classes

<!-- image -->

## Exemplo prático

Vamos começar criando a nossa classe que irá representar o nosso carro ela irá chamar Vehicle, com o seguinte código:

```
public class Vehicle{public string Model { get; set; }public string Engine { get; set; }public string Transmission { get; set; }public string Body { get; set; }public List<string> Accessories { get; set; }public Vehicle(){Accessories = new List<string>();}public void ShowInfo(){Console.WriteLine("Model: {0}", Model);Console.WriteLine("Engine: {0}", Engine);Console.WriteLine("Body: {0}", Body);Console.WriteLine("Transmission: {0}", Transmission);Console.WriteLine("Accessories:");foreach (var accessory in Accessories){Console.WriteLine("\t{0}", accessory);}}
```

em seguida iremos criar a interface que será usada como nosso builder que terá o seguinte código:

```
public interface IVehicleBuilder{void SetModel();void SetEngine();void SetTransmission();void SetBody();void SetAccessories();Vehicle GetVehicle();}
```

Criei os métodos que representam as partes do carro que iremos criar. Em seguida criei a classe concreta para o nosso builder.

Abaixo a minha classe HondaBuilder que implementa a IVehicleBuilder.

```
public class HondaBuilder : IVehicleBuilder{Vehicle objVehicle = new Vehicle();public void SetModel(){objVehicle.Model = "Honda";}public void SetEngine(){objVehicle.Engine = "4 Stroke";}public void SetTransmission(){objVehicle.Transmission = "125 Km/hr";}public void SetBody(){objVehicle.Body = "Plastic";}public void SetAccessories(){objVehicle.Accessories.Add("Seat Cover");objVehicle.Accessories.Add("Rear Mirror");objVehicle.Accessories.Add("Helmet");}public Vehicle GetVehicle(){return objVehicle;}}
```

Criei também uma classe FerrariBuilder que implementa a IVehicleBuilder.

```
public class FerrariBuilder : IVehicleBuilder{Vehicle objVehicle = new Vehicle();public void SetModel(){objVehicle.Model = "Ferrari 360";}public void SetEngine(){objVehicle.Engine = "4 Stroke";}public void SetTransmission(){objVehicle.Transmission = "280 Km/hr";}public void SetBody(){objVehicle.Body = "Glass Fiber";}public void SetAccessories(){objVehicle.Accessories.Add("Seat Cover");objVehicle.Accessories.Add("Rear Mirror");objVehicle.Accessories.Add("Helmet");}public Vehicle GetVehicle(){return objVehicle;}}
```

O próximo passo é criar nosso Director, ele irá conter o seguinte código

```
public class VehicleCreator{private readonly IVehicleBuilder objBuilder;public VehicleCreator(IVehicleBuilder builder){objBuilder = builder;}public void CreateVehicle(){objBuilder.SetModel();objBuilder.SetEngine();objBuilder.SetBody();objBuilder.SetTransmission();objBuilder.SetAccessories();}public Vehicle GetVehicle(){return objBuilder.GetVehicle();}}
```

Vale ressaltar que esse pattern deve ser aplicado conforme seu contexto, porém diferente de alguns outros é possível seguir uma "receita" na hora de implementar, mas ainda assim uma aplicação de produção não ficaria 100% igual ao nosso exemplo.

Em seguida criar os métodos de construção a nossa classe Program.cs do nosso aplicativo de console

```
class Program{static void Main(string[] args){var vehicleCreator = new VehicleCreator(new FerrariBuilder());vehicleCreator.CreateVehicle();var vehicle = vehicleCreator.GetVehicle();vehicle.ShowInfo();Console.WriteLine("---------------------------------------------");vehicleCreator = new VehicleCreator(new HondaBuilder());vehicleCreator.CreateVehicle();vehicle = vehicleCreator.GetVehicle();vehicle.ShowInfo();Console.ReadKey();}}
```

Nesse exemplo eu acabei criando uma casa "customizada" para exemplificar como poderiamos simplesmente criar um o objeto customizado.

Bom pessoal vou ficando por aqui.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsCsharpXp IncXp Investimentos

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