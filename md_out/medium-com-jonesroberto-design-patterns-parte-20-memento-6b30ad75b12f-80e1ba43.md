---
title: "https://medium.com/@jonesroberto/design-patterns-parte-20-memento-6b30ad75b12f"
source_url: "https://medium.com/@jonesroberto/design-patterns-parte-20-memento-6b30ad75b12f"
---
# Design Patterns - Parte 20- Memento

Jones Roberto Nuzzi4 min read·Jan 21, 2020

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite salvar e restaurar o estado anterior de um objeto sem revelar os detalhes de sua implementação.

# Problema

Você precisa restaurar um objeto de volta ao seu estado anterior (por exemplo, operações "desfazer" ou "reverter").

# Solução

O cliente solicita um Memento do objeto de origem quando precisa verificar o estado do objeto de origem. O objeto de origem inicializa o Memento com uma caracterização de seu estado. O cliente é o "care-taker" do Memento, mas apenas o objeto de origem pode armazenar e recuperar informações do Memento (o Memento é "opaco" para o cliente e todos os outros objetos). Se o cliente precisar subseqüentemente "reverter" o estado do objeto de origem, ele entregará o Memento de volta ao objeto de origem para reintegração.

# Implementação

O diagrama de classes UML para a implementação do Memento Design Pattern é apresentado abaixo:

<!-- image -->

# Prós

- Você pode produzir instantâneos do estado do objeto sem violar seu encapsulamento.
- Você pode simplificar o código do autor, deixando o responsável manter o histórico do estado do autor.

# Contras

- O aplicativo pode consumir muita RAM se os clientes criarem mementos com muita frequência.
- Os responsáveis devem acompanhar o ciclo de vida do remetente para poder destruir mementos obsoletos.
- A maioria das linguagens de programação dinâmicas, como PHP, Python e JavaScript, não pode garantir que o estado no memento permaneça intacto.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Originator

Esta é uma classe que cria um objeto de lembrança contendo um instante do estado atual do "Originator". Ele também restaura o "Originator" para um estado armazenado anteriormente usando a operação Save.

## ConcreteMemento

Esta é uma interface que contém as informações sobre o estado salvo do "Originator".

## Memento

Esta é uma interface que contém as abstrações necessárias para implementação da ConcreteMemento.

## Caretaker

Esta é uma classe usada para armazenar um objeto Memento para uso posterior. Isso funciona apenas como uma loja; nunca examina ou modifica o conteúdo do objeto Memento.

## Exemplo prático

Bom vamos lá, primeiramente irei criar uma interface IMemento, que irá conter o seguinte código:

```
public interface IMemento{string GetName();string GetState();DateTime GetDate();}
```

Em seguida irei adicionar uma classe concreta que implementa nosso memento, que irá conter o seguinte código:

```
class ConcreteMemento : IMemento{private string _state;private DateTime _date;public ConcreteMemento(string state){this._state = state;this._date = DateTime.Now;}public string GetState(){return this._state;}public string GetName(){return $"{this._date} / ({this._state.Substring(0, 9)})...";}public DateTime GetDate(){return this._date;}}
```

Em seguida irei criar nosso Originator, que irá conter o seguinte código:

```
public class Originator{private string _state;public Originator(string state){this._state = state;Console.WriteLine("Originator: My initial state is: " + state);}public void DoSomething(){Console.WriteLine("Originator: I'm doing something important.");this._state = this.GenerateRandomString(30);Console.WriteLine($"Originator: and my state has changed to: {_state}");}private string GenerateRandomString(int length = 10){string allowedSymbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";string result = string.Empty;while (length > 0){result += allowedSymbols[new Random().Next(0, allowedSymbols.Length)];Thread.Sleep(12);length--;}return result;}// Saves the current state inside a memento.public IMemento Save(){return new ConcreteMemento(this._state);}// Restores the Originator's state from a memento object.public void Restore(IMemento memento){if (!(memento is ConcreteMemento)){throw new Exception("Unknown memento class " + memento.ToString());}this._state = memento.GetState();Console.Write($"Originator: My state has changed to: {_state}");}}
```

Em seguida irei criar nosso Caretaker, que irá conter o seguinte código:

```
class Caretaker{private List<IMemento> _mementos = new List<IMemento>();private Originator _originator = null;public Caretaker(Originator originator){this._originator = originator;}public void Backup(){Console.WriteLine("\nCaretaker: Saving Originator's state...");this._mementos.Add(this._originator.Save());}public void Undo(){if (this._mementos.Count == 0){return;}var memento = this._mementos.Last();this._mementos.Remove(memento);Console.WriteLine("Caretaker: Restoring state to: " + memento.GetName());try{this._originator.Restore(memento);}catch (Exception){this.Undo();}}public void ShowHistory(){Console.WriteLine("Caretaker: Here's the list of mementos:");foreach (var memento in this._mementos){Console.WriteLine(memento.GetName());}}}
```

E por fim irei alterar nossa classe Program.cs para conseguir testar nosso Memento, ela irá ficar com o seguinte código:

```
class Program{static void Main(string[] args){// Client code.Originator originator = new Originator("Super-memento.");Caretaker caretaker = new Caretaker(originator);caretaker.Backup();originator.DoSomething();caretaker.Backup();originator.DoSomething();caretaker.Backup();originator.DoSomething();Console.WriteLine();caretaker.ShowHistory();Console.WriteLine("\nClient: Now, let's rollback!\n");caretaker.Undo();Console.WriteLine("\n\nClient: Once more!\n");caretaker.Undo();Console.WriteLine();}}
```

Bom pessoal, espero que o exemplo ajude a conseguir implementar o memento no mundo real, até próxima, Abraço

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Desing PatternDesign PatternsXp Inc

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