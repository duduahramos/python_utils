---
title: "https://medium.com/xp-inc/desing-patterns-parte-10-composite-f7600cb3aad7"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-10-composite-f7600cb3aad7"
---
# Design Patterns - Parte 10 - Composite

Jones Roberto Nuzzi4 min read·Nov 14, 2019

--

Share

<!-- image -->

# Intenção

Composite é um padrão de design estrutural que permite compor objetos em estruturas de árvores e trabalhar com essas estruturas como se fossem objetos individuais. Com ele você pode:

- Compor objetos em estruturas de árvore para representar hierarquias de peças inteiras. Composite permite que os clientes tratem objetos individuais e composições de objetos de maneira uniforme.
- Composição recursiva
- "Diretórios contêm entradas, cada uma das quais poderia ser um diretório."
- 1-para-muitos "tem uma hierarquia" acima da "é uma"

# Problema

O aplicativo precisa manipular uma coleção hierárquica de objetos "primitivos" e "compostos". O processamento de um objeto primitivo é tratado de uma maneira, e o processamento de um objeto composto é tratado de maneira diferente. Ter que consultar o "tipo" de cada objeto antes de tentar processá-lo não é desejável.

# Solução

O padrão composite compõe objetos em termos de uma estrutura em árvore para representar partes e hierarquias inteiras.

A chave para o padrão composite é uma classe abstrata que representa tanto o objeto primitivo como os seus recipientes.

# Implementação

O diagrama de classes UML para a implementação do padrão de design composto é apresentado abaixo:

<!-- image -->

As classes, interfaces e objetos no diagrama de classes UML acima são os seguintes:

## Component

Esta é uma classe abstrata que contém membros que serão implementados por todos os objetos na hierarquia. Ele atua como a classe base para todos os objetos dentro da hierarquia

## Leaf

Esta é uma classe usada para definir componentes de folhas na estrutura da árvore, pois estes não podem ter filhos.

## Composite

Esta é uma classe que inclui os métodos Adicionar, Remover, Localizar e Obter para executar operações em componentes filhos.

## Prós

- Você pode trabalhar com estruturas de árvores complexas de maneira mais conveniente: use polimorfismo e recursão a seu favor.
- Princípio Aberto/Fechado . Você pode introduzir novos tipos de elementos no aplicativo sem quebrar o código existente, que agora funciona com a árvore de objetos.

# Contras

- Pode ser difícil fornecer uma interface comum para classes cuja funcionalidade difere demais. Em certos cenários, você precisaria generalizar demais a interface do componente, dificultando a compreensão.

# Exemplo

## Uso do padrão em C#

<!-- image -->

## O que é oque?

1. IEmployed - Interface Component.
2. Employee- classe Composite.
3. Contractor- classe Leaf .

## Diagrama de classes

<!-- image -->

## Exemplo prático

Bom vamos para o exemplo prático do padrão composite. Vamos começar criando nosso 'Component' essa interface irá IEmployed, e irá conter o seguinte código:

```
public interface IEmployed{int EmpID { get; set; }string Name { get; set; }}
```

Em seguida iremos adicionar nosso 'Composite', irei chamar nossa classe de Employee e ela irá implementar a interface IEmployed, e um enumerable de IEmployed conforme código a seguir:

```
public class Employee : IEmployed, IEnumerable<IEmployed>{private List<IEmployed> _subordinates = new List<IEmployed>();public int EmpID { get; set; }public string Name { get; set; }public void AddSubordinate(IEmployed subordinate){_subordinates.Add(subordinate);}public void RemoveSubordinate(IEmployed subordinate){_subordinates.Remove(subordinate);}public IEmployed GetSubordinate(int index){return _subordinates[index];}public IEnumerator<IEmployed> GetEnumerator(){foreach (IEmployed subordinate in _subordinates){yield return subordinate;}}IEnumerator IEnumerable.GetEnumerator(){return GetEnumerator();}}
```

Em seguida iremos adicionar nosso 'Leaf', que irá chamar Contractor e também irá implementar IEmployed, e irá conter o seguinte código:

```
public class Contractor : IEmployed{public int EmpID { get; set; }public string Name { get; set; }}
```

agora irei modificar nossa classe Program do console para podermos testar nosso Composite, e ela ficará com o código a seguir:

```
class Program{static void Main(string[] args){Employee Thiago = new Employee { EmpID = 1, Name = "Thiago" };Employee Gabriel = new Employee { EmpID = 2, Name = "Gabriel" };Employee Jones = new Employee { EmpID = 3, Name = "Jones" };Thiago.AddSubordinate(Gabriel);Thiago.AddSubordinate(Jones);Employee Barbara = new Employee { EmpID = 4, Name = "Barbara" };Employee Andre = new Employee { EmpID = 5, Name = "André" };Gabriel.AddSubordinate(Barbara);Gabriel.AddSubordinate(Andre);Employee Cesar = new Employee { EmpID = 6, Name = "Cesar" };Employee Igor = new Employee { EmpID = 7, Name = "Igor" };Contractor Gisnando = new Contractor { EmpID = 8, Name = "Gisnando" };Contractor Gerlandio = new Contractor { EmpID = 9, Name = "Gerlandio" };Jones.AddSubordinate(Cesar);Jones.AddSubordinate(Igor);Jones.AddSubordinate(Gisnando);Jones.AddSubordinate(Gerlandio);Console.WriteLine($"EmpID={Thiago.EmpID}, Name={Thiago.Name}");foreach (Employee manager in Thiago){Console.WriteLine($"\n EmpID={manager.EmpID}, Name={manager.Name}");foreach (var employee in manager){Console.WriteLine($" \t EmpID={employee.EmpID}, Name={employee.Name}");}}Console.ReadKey();}}
```

Bom, espero que o exemplo seja simples de entender, qualquer dúvida entre me contato, vou ficando por aqui. Até a próxima.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design PatternsCsharpXp IncLab Xp

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