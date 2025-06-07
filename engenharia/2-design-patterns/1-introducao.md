# Design Patterns - Padrões de Projeto

## Introdução

Como em toda engenharia, a Engenharia de Software também busca padronizar soluções para problemas recorrentes. Essa padronização permite criar soluções e artefatos reutilizáveis em diferentes contextos, tornando a resolução de problemas mais rápida e eficiente.

Vamos imaginar, por exemplo, na Engenharia Mecânica, o problema de unir duas peças. Esse desafio pode ser resolvido de diferentes formas: solda, parafuso, cola, entre outras. Cada solução tem vantagens e desvantagens específicas para diferentes contextos.

Tomemos o parafuso como exemplo. Hoje estamos familiarizados com os diversos tipos de parafusos e suas aplicações. Porém, no início, o parafuso era uma inovação sem padronização (aliás, até hoje temos problemas com isso, como as diferenças entre medidas métricas e padrão imperial). Imagine a dificuldade: cada pessoa que precisasse unir duas peças teria que fabricar seu próprio parafuso, com características únicas. Embora o problema inicial fosse resolvido, qualquer manutenção posterior exigiria ferramentas específicas para aquele parafuso particular, tornando o processo caro e complexo.

Para simplificar a tarefa que hoje consideramos trivial de apertar ou soltar um parafuso, foi necessário criar normas e padrões para os diversos tipos de parafusos. Isso possibilitou o desenvolvimento de ferramentas universais, tornando a solução mais rápida e eficiente.

[Este post](https://projetosmecanicos.wordpress.com/2011/11/16/normas-de-parafusos/) exemplifica os padrões criados para parafusos. Note que os padrões não são os parafusos em si, nem as ferramentas para manipulá-los, mas formas de descrever características, aplicações, vantagens e desvantagens dos diversos tipos. Cabe ao profissional escolher o melhor tipo considerando o contexto específico.

Portanto, nosso objetivo aqui não é criar soluções prontas (parafusos prontos), mas padronizar abordagens para resolver problemas comuns. Estamos criando formas de pensar e abordar desafios recorrentes em diferentes contextos, possibilitando soluções reutilizáveis que tornam a resolução de problemas mais eficiente.

## O que são Design Patterns?

Design Patterns são conceitos, métodos ou teorias que descrevem soluções para problemas comuns no desenvolvimento de software. São descrições ou modelos aplicáveis a diferentes situações, auxiliando na resolução eficiente e eficaz de problemas.

Assim, Design Patterns não são códigos prontos, mas formas de pensar e abordar problemas comuns em diferentes contextos. Eles padronizam soluções para desafios recorrentes no desenvolvimento de software, tornando a resolução mais rápida e eficiente.

Por isso, você não pode simplesmente encontrar um Design Pattern e copiá-lo para seu código. Diferentemente de um algoritmo (como verificar se um número é primo), o Design Pattern é uma abordagem conceitual para tipos específicos de problemas.

Portanto, não confunda Design Patterns com algoritmos. Embora ambos descrevam soluções para problemas conhecidos, são diferentes: o Design Pattern é uma forma de pensar e abordar problemas comuns em diversos contextos, enquanto o algoritmo é uma sequência específica de passos para resolver um problema particular.

## Formalização de Design Patterns

A maioria dos Design Patterns segue um padrão formal de descrição que permite sua aplicação em diferentes contextos. Basicamente, essa descrição divide-se nas seguintes partes:

1. **Nome**: Identificação do padrão
2. **Propósito**: Determina e descreve brevemente o problema a resolver e a solução proposta
3. **Motivação**: Explica detalhadamente o problema que o padrão resolve e sua solução
4. **Estrutura**: Descreve a composição do padrão e suas relações com outros padrões
5. **Consequências**: Apresenta os efeitos de utilizar o padrão, incluindo vantagens e desvantagens

Alguns padrões podem incluir seções adicionais, como exemplos de código, etapas de implementação ou relações com outros padrões. Contudo, essas cinco partes constituem a base mais comum encontrada na maioria dos padrões.