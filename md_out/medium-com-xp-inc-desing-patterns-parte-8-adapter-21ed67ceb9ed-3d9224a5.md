---
title: "https://medium.com/xp-inc/desing-patterns-parte-8-adapter-21ed67ceb9ed"
source_url: "https://medium.com/xp-inc/desing-patterns-parte-8-adapter-21ed67ceb9ed"
---
# Design Patterns - Parte 8 - Adapter

Jones Roberto Nuzzi4 min read·Nov 7, 2019

--

Share

<!-- image -->

# Intenção

- Converta a interface de uma classe em outra interface que os clientes esperam. O adapter permite que as classes trabalhem juntas que não poderiam de outra forma por causa de interfaces incompatíveis.
- Agrupe uma classe existente com uma nova interface.
- A impedância corresponde a um componente antigo a um novo sistema

# Problema

Imagine que você está criando um aplicativo de monitoramento do mercado de ações. O aplicativo baixa os dados de estoque de várias fontes no formato XML e exibe gráficos e diagramas de boa aparência para o usuário.

Em algum momento, você decide melhorar o aplicativo integrando uma biblioteca de análise inteligente de terceiros. Mas há um problema: a biblioteca de análise funciona apenas com dados no formato JSON.

<!-- image -->

Você não pode usar a biblioteca de análise "como está", pois espera os dados em um formato incompatível com seu aplicativo.

Você pode alterar a biblioteca para trabalhar com XML. No entanto, isso pode quebrar algum código existente que depende da biblioteca. E pior, você pode não ter acesso ao código-fonte da biblioteca em primeiro lugar, tornando essa abordagem impossível.

# Solução

# Implementação

<!-- image -->

## ITarget

- Essa é uma interface usada pelo cliente para atingir sua funcionalidade / solicitação.

## Adapter

Esta é uma classe que implementa a interface ITarget e herda a classe Adaptee. É responsável pela comunicação entre o Client e o Adaptee.

## Adaptee

Esta é uma classe que possui a funcionalidade exigida pelo Client. No entanto, sua interface não é compatível com o Client.

## Client

Esta é uma classe que interage com um tipo que implementa a interface ITarget. No entanto, a classe de comunicação denominada Adaptee não é compatível com o Client.

# Prós

- Princípio de responsabilidade única . Você pode separar a interface ou o código de conversão de dados da lógica de negócios principal do programa.
- Princípio Aberto / Fechado . Você pode introduzir novos tipos de adaptadores no programa sem quebrar o código do cliente existente, desde que eles funcionem com os adaptadores por meio da interface do cliente.

# Contras

A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes. Às vezes, é mais simples alterar a classe de serviço para que corresponda ao restante do seu código.

# Exemplo

Diagrama de classes

<!-- image -->

# O que é o que?

As classes, interfaces e objetos no diagrama de classes acima podem ser identificados da seguinte

1. ITarget - interface Target
2. EmployeeAdapter- Adapter
3. HRSystem- classe Adaptee
4. ThirdPartyBillingSystem - Client

Primeiramente irei criar a interface ITarget, com o seguinte código:

```
public interface ITarget{List<string> GetEmployeeList();}
```

Em seguida irei criar a classe Client ela será chamada de ThirdPartyBillingSystem, com o seguinte código:

```
public class ThirdPartyBillingSystem{private ITarget employeeSource;public ThirdPartyBillingSystem(ITarget employeeSource){this.employeeSource = employeeSource;}public void ShowEmployeeList(){List<string> employee = employeeSource.GetEmployeeList();//To DO: Implement you business logicConsole.WriteLine("######### Lista de  funcionários ##########");foreach (var item in employee){Console.Write(item);}}}
```

Na sequência irei criar a classe HRSystem, com o seguinte código:

```
public class HRSystem{public string[][] GetEmployees(){string[][] employees = new string[4][];employees[0] = new string[] { "100", "Cesar Silva", "Coordenador de TI" };employees[1] = new string[] { "101", "Igor Kawata", "Coordenador de TI" };employees[2] = new string[] { "102", "Renato Novelli", "Desenvolvedor Senior" };employees[3] = new string[] { "103", "André Cirelli", "Product Owner" };return employees;}}
```

E por ultimo iremos criar a classe EmployeeAdapter que irá herdar HRSystem e também irá implementar a interface ITarget, com o seguinte código:

```
public class EmployeeAdapter : HRSystem, ITarget{public List<string> GetEmployeeList(){List<string> employeeList = new List<string>();string[][] employees = GetEmployees();foreach (string[] employee in employees){employeeList.Add(employee[0]);employeeList.Add(",");employeeList.Add(employee[1]);employeeList.Add(",");employeeList.Add(employee[2]);employeeList.Add("\n");}return employeeList;}}
```

E por fim, iremos modificar nossa classe Program, para que seja possivel ver nosso design funcionando, com o seguinte código:

```
class Program{static void Main(string[] args){ITarget Itarget = new EmployeeAdapter();ThirdPartyBillingSystem client = new ThirdPartyBillingSystem(Itarget);client.ShowEmployeeList();Console.ReadKey();}}
```

Como é possível observar o padrão adapter torna bem mais simples a conversão de um tipo em outro, esse padrão é muito útil para o caso de DDD, onde muitas vezes você precisa consumir dados externos e adaptar para compor seu domínio, esse padrão tornaria mais simples a conversão de dados.

Bom vou ficando por aqui, na próxima semana irei falar do padrão Bridge, até mais pessoal.

# Para saber Mais

## Todos os links sobre Design Patterns e GitHub

## Design Patterns

### Boa noite Pessoal, como nossa postagem será dividida em 24 partes estou criando essa história para concentrar todos os...

medium.com

Xp IncXp InvestimentosDesign PatternsDotnet Core

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