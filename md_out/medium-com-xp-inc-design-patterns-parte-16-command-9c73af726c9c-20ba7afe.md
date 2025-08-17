---
title: "https://medium.com/xp-inc/design-patterns-parte-16-command-9c73af726c9c"
source_url: "https://medium.com/xp-inc/design-patterns-parte-16-command-9c73af726c9c"
---
# Design Patterns - Parte 16 - Command

Jones Roberto Nuzzi4 min read·Dec 18, 2019

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que transforma uma solicitação em um objeto independente que contém todas as informações sobre a solicitação. Essa transformação permite parametrizar métodos com diferentes solicitações, atrasar ou enfileirar a execução de uma solicitação e oferecer suporte a operações que podem ser desfeitas.

# Problema

É necessário emitir solicitações para objetos sem saber nada sobre a operação que está sendo solicitada ou o destinatário da solicitação.

# Solução

O command desacopla o objeto que chama a operação daquele que sabe como executá-la. Para conseguir essa separação, o designer cria uma classe base abstrata que mapeia um receiver (um objeto) com uma ação (um ponteiro para uma função de um membro). A classe base contém um método Execute() que simplesmente chama a ação no "receiver".

Todos os clientes dos objetos Command tratam cada objeto como uma "caixa preta", simplesmente invocando o método virtual Execute() sempre que o cliente exigir o "serviço" do objeto.

Uma classe Command contém alguns subconjuntos do seguinte: um objeto, um método a ser aplicado ao objeto e os argumentos a serem transmitidos quando o método é chamado. O método Execute() do Command faz com que as peças se juntem.

# Implementação

O diagrama de classes UML para a implementação do padrão de design do comando é fornecido abaixo:

<!-- image -->

# Prós

- Princípio de responsabilidade única . Você pode desacoplar classes que invocam operações de classes que executam essas operações.
- Princípio Aberto / Fechado . Você pode introduzir novos comandos no aplicativo sem quebrar o código do cliente existente.
- Você pode implementar desfazer / refazer.
- Você pode implementar a execução adiada de operações.
- Você pode montar um conjunto de comandos simples em um complexo.

# Contras

O código pode se tornar mais complicado, pois você está introduzindo uma nova camada entre remetentes e receptores.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Cliente

Esta é a classe que cria e executa o objeto de command.

## Invoker

Solicita ao command para executar a ação.

## Command

Esta é uma interface que especifica a operação Execute.

## ConcreteCommand

Esta é uma classe que implementa a operação Execute invocando operações no Receiver.

## Receiver

Esta é uma classe que executa a Ação associada à solicitação.

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos lá, primeiramente irei criar a interface Command, que irá conter o seguinte código:

```
public interface ICommand{void Execute();}
```

em seguida iremos criar a classe Invoker que irá conter o seguinte código:

```
public class Switch{private List<ICommand> _commands = new List<ICommand>();public void StoreAndExecute(ICommand command){_commands.Add(command);command.Execute();}}
```

Agora vamos criar o nosso Receiver, que irá conter o seguinte código:

```
public class Light{public void TurnOn(){Console.WriteLine("The light is on");}public void TurnOff(){Console.WriteLine("The light is off");}}
```

Agora iremos criar os command para mexer acender e apagar nossas luzes, quer irão conter o seguinte código:

- FlipUp Command que irá implementar ICommand

```
public class FlipUpCommand : ICommand{private Light _light;public FlipUpCommand(Light light){_light = light;}public void Execute(){_light.TurnOn();}}
```

- FlipDownCommand que também irá implementar ICommand

```
public class FlipDownCommand : ICommand{private Light _light;public FlipDownCommand(Light light){_light = light;}public void Execute(){_light.TurnOff();}}
```

E por último iremos modificar nossa classe Program.cs para utilizar nosso Command, e ela irá ficar com o seguinte código:

```
class Program{static void Main(string[] args){Console.WriteLine("Enter Commands (ON/OFF) : ");string cmd = Console.ReadLine();Light lamp = new Light();ICommand switchUp = new FlipUpCommand(lamp);ICommand switchDown = new FlipDownCommand(lamp);Switch s = new Switch();if (cmd == "ON"){s.StoreAndExecute(switchUp);}else if (cmd == "OFF"){s.StoreAndExecute(switchDown);}else{Console.WriteLine("Command \"ON\" or \"OFF\" is required.");}Console.ReadKey();}}
```

Nesse exemplo criei um command simples onde é possível ligar ou desligar uma lâmpada, daria para usarmos reflection para localizar todos que implementam a interface ICommand e também utilizar injeção de dependência para fazermos os chamadas de liga e desliga, porém quis manter o mais simples possível, vou ficando por aqui pessoal até a próxima

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsGofArquitetura SoftwareCsharp

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