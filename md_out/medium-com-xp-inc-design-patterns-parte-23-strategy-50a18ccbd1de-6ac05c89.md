---
title: "https://medium.com/xp-inc/design-patterns-parte-23-strategy-50a18ccbd1de"
source_url: "https://medium.com/xp-inc/design-patterns-parte-23-strategy-50a18ccbd1de"
---
# Design Patterns - Parte 23 - Strategy

Jones Roberto Nuzzi4 min read·Mar 4, 2020

--

Share

<!-- image -->

# Intenção

É um padrão de design comportamental que permite definir uma família de algoritmos, colocar cada um deles em uma classe separada e tornar seus objetos intercambiáveis.

# Problema

O problema principal que o strategy tenta resolver, é diminuir o acoplamento entre classes bases de classes derivadas.

como isso ele acaba indo de encontro a um dos princípios do solid "principle open-closed".

# Solução

Encapsule detalhes da interface em uma classe base e oculte detalhes da implementação em classes derivadas. Os clientss podem, então, se acoplar a uma interface e não precisam se modificados: com isso, nosso client não sofreria nenhum impacto quando o número de classes derivadas é alterado e nenhum impacto quando a implementação de uma classe derivada é alterada.

# Implementação

O diagrama de classes UML para a implementação do Padrão de Design da Estratégia é apresentado abaixo:

<!-- image -->

# Prós

- Você pode trocar algoritmos usados dentro de um objeto em tempo de execução.
- Você pode isolar os detalhes de implementação de um algoritmo do código que o utiliza.
- Você pode substituir herança por composição.
- Princípio Aberto / Fechado . Você pode introduzir novas estratégias sem precisar alterar o contexto.

# Contras

- Se você possui apenas alguns algoritmos e eles raramente mudam, não há motivo real para complicar demais o programa com novas classes e interfaces que acompanham o padrão.
- Os clientes devem estar cientes das diferenças entre as estratégias para poder selecionar uma adequada.
- Muitas linguagens de programação modernas têm suporte ao tipo funcional que permite implementar versões diferentes de um algoritmo dentro de um conjunto de funções anônimas. Então você poderia usar essas funções exatamente como usaria os objetos de estratégia, mas sem inchar seu código com classes e interfaces extras.

# Exemplo

## Uso do padrão

<!-- image -->

## O que é oque?

## Context

Esta é uma classe que contém uma propriedade para manter a referência de um objeto de Estratégia. Esta propriedade será configurada em tempo de execução de acordo com o algoritmo necessário.

## Strategy

Essa é uma interface usada pelo objeto Context para chamar o algoritmo definido por uma ConcreteStrategy.

## ConcreteStrategy

Essas são classes que implementam a interface da strategy.

# Quando usar?

1. Existem várias estratégias para um determinado problema e os critérios de seleção de uma estratégia são definidos como um tempo de execução.
2. Muitas classes relacionadas diferem apenas em seus comportamentos.
3. As estratégias usam os dados aos quais o cliente não tem acesso.

## Exemplo prático

Bom vamos lá, vou tentar usar um exemplo que se parece com um exemplo que acabei implementando na vida real, vou começar pela interface IStrategy

```
interface IStrategy{CustomerPositionModel GetCustomerPosition(long customerCode);}
```

Na nossa interface eu acabei criando uma model para nos auxiliar em nossa implementação de strategy, ela vai se chamar CustomerPositionModel, e irá conter o seguinte código:

```
public class CustomerPositionModel{public string Name { get; set; }public decimal Value { get; set; }}
```

Em seguida irei criar a classe Context, e ela irá conter o seguinte código:

```
class Context{private IStrategy _strategy;public Context(){ }public Context(IStrategy strategy){this._strategy = strategy;}public void SetStrategy(IStrategy strategy){this._strategy = strategy;}public void GetCustomerPosition(long customerCode){var result = this._strategy.GetCustomerPosition(customerCode);Console.WriteLine($"Customer: {result.Name} - Position {result.Value}");}}
```

Em seguida irei criar as classes concretas do nosso strategy

- PositionEquities, que irá implementar a interface IStrategy

```
class PositionEquities : IStrategy{public CustomerPositionModel GetCustomerPosition(long customerCode){if (customerCode > 0){var result=  new CustomerPositionModel{Name = $"Cliente {customerCode}",Value = 100000};Console.WriteLine($"{result.Name} - {result.Value}");return result;}return new CustomerPositionModel();}}
```

- PositionFunds, que também irá implementar a interface IStrategy

```
public class PositionFunds : IStrategy{public CustomerPositionModel GetCustomerPosition(long customerCode){if (customerCode > 0){var result = new CustomerPositionModel{Name = $"Cliente {customerCode}",Value = 2000};Console.WriteLine($"{result.Name} - {result.Value}");return result;}return new CustomerPositionModel();}}
```

Agora por último vamos modificar a classe Program.cs, e ela irá conter o seguinte código:

```
class Program{static void Main(string[] args){var context = new Context();Console.WriteLine("Client: ");context.SetStrategy(new PositionEquities());context.GetCustomerPosition(335962);Console.WriteLine();Console.WriteLine("Client: ");context.SetStrategy(new PositionFunds());context.GetCustomerPosition(335962);}}
```

Bom vou ficando por aqui pessoal, espero que o exemplo fique claro da utilidade desse pattern que é um dos meus preferidos.Até a próxima.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Design Patterns

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