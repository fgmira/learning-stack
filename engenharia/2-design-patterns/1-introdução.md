# Design Patterns - Padrões de Projeto

## Introdução

Como toda a engenharia, inclusive na Engenharia de Software, ocorre uma tentativa de buscar uma certa padronização de soluções dadas a problemas que normalmente as engenharias tendem a resolver.

Essa busca de padronização de soluções e por consequência, a padronização de problemas, possibilita a criação de soluções e artefatos que podem ser reutilizados em diferentes contextos, o que torna a solução de problemas mais rápida e eficiente.

Vamos imaginar, por exemplo, na Engenhria Mecânica, o problema de se juntar duas peças. Esse problema pode ser resolvido de diferentes formas, como por exemplo, solda, parafuso, cola, etc. Cada uma dessas soluções tem suas vantagens e desvantagens e são aplicadas em diferentes contextos.

Pegando o parafuso como exemplo. Hoje estamos acostumados com os diversos tipos de parafusos e suas aplicabilidades. Mas, no início, o parafuso era uma inovação e não existia um padrão de como ele deveria ser feito (Aliás até hoje a gente tem problemas com isso, por exemplo padões em medidas métricas e outro em padrão imperial). Imagina a dificuldade que era utilizar esse tipo de solução: Cada pessoa que iria realizar esse tipo de junção teria que fabricar o seu próprio parafuso, da sua forma e com suas características. Num primeiro momento, o problema de juntar duas peças foi resolvido, mas quando alguem fosse dar uma manutenção nessa junção, teria que fabricar todo um ferramental para conseguir retirar o parafuso que foi feito de uma forma diferente do que ele estava acostumado. Isso tornaria a manutenção desse tipo de junção muito mais cara e complexa. Para tornar simples a tarefa que temos hoje de apertar ou soltar um parafuso, foi necessário criar uma série de normas e padrões de como os diversos tipos de parafusos deveriam ser feitos. Isso possibilitou a criação de ferramentas que podem ser utilizadas em diferentes contextos, o que torna a solução do problema de se fixar duas coisas mais rápida e eficiente.

[Aqui](https://projetosmecanicos.wordpress.com/2011/11/16/normas-de-parafusos/) vemos um post de um blog que fala sobre esses padrões que foram criados para os parafusos. Perceba que os padrões não são os parafusos em si, nem as ferramentas uilizadas para manipula-los, mas uma forma de descrever diversas formas e caracteristicas de como são os diversos tipos de parafusos e suas aplicabilidades, com suas vantagens e desvantagens. Cabe a pessoa que vai resolver o problema de juntar duas peças escolher qual o melhor tipo de parafuso a ser utilizado, levando em consideração o contexto em que esse desafio se encontra.

Portanto, o que estamos fazendo aqui é uma tentativa de padronizar soluções para se resolver problemas e não uma tentativa de criar soluções prontas (parafusos prontos). O que estamos fazendo é criar uma forma de pensar e abordar problemas comuns que podem ser encontrados em diferentes contextos. Isso possibilita a criação de soluções e artefatos que podem ser reutilizados em diferentes contextos, o que torna a solução de problemas mais rápida e eficiente.


## O que são Design Patterns?

Os Design Patterns são idéias, métodos ou teorias de soluções para problemas comuns que ocorrem no desenvolvimento de software. Eles são descrições ou modelos que podem ser aplicados a diferentes situações, ajudando a resolver problemas de forma mais eficiente e eficaz.

Sendo assim, Design Patterns não são códigos prontos, mas sim uma forma de pensar e abordar problemas comuns que podem ser encontrados em diferentes contextos. Eles são uma forma de padronizar soluções para problemas comuns encontrados no desenvolvimento de software, tornando a solução de problemas mais rápida e eficiente.

Dessa forma você não pode simplesmente encontrar um Design Pattern, copia-lo e colar no seu código. O Design Pattern não é um trecho de código, como um algoritmo para ver se um número é primo ou não. O Design Pattern é uma forma de pensar e abordar um ou mais determinados tipos de problemas.

Portanto não confunda Design Patterns com algoritmos, embora ambos descrevam soluções para problemas típicos e conhecidos, eles são diferentes. O Design Pattern é uma forma de pensar e abordar problemas comuns que podem ser encontrados em diferentes contextos, enquanto o algoritmo é uma sequência de passos para resolver um problema específico.

## Formalização de Design Patterns

A maioria dos Design Patterns seguem meio que um padrão formal de descrição que permite que as pessoas possam aplica-los em diferentes contextos. Basicamente, esse padrão de descrição é dividido nas seguintes partes:
1. **Nome**: Nome do padrão
2. **Propósito**: Determina e descreve brevemente o problema que tenta resolver e a solução que propõe.
3. **Motivação**: Explica mais a fundo o problema que o padrão tenta resolver e a solução que propõe. 
4. **Estrutura**: Descreve a estrutura do padrão, como ele é composto e como ele se relaciona com outros padrões.
5. **Consequências**: Descreve as consequências de se utilizar o padrão, como ele pode afetar o sistema e quais são suas vantagens e desvantagens.

Alguns padrões podem ter mais partes, como por exemplo, exemplos de código, etapas de implementação, relações com outros padrões, etc. Mas essas cinco partes são as mais comuns e básicas que você vai encontrar na maioria dos padrões.

