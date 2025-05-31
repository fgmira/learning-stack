# Princípios de Projetos de Software

## Introdução

Os pincípios de projetos de software são diretrizes fundamentais que orientam como escrever, organizar e estruturar um código com qualidade, ou seja, como criar um código que seja fácil de entender, fácil de manter e fácil de evoluir. Esses princípios representam uma base conceitual por trás de um bom design de software e servem como critério para avaliar se um código está bem estruturado ou não.

Esses princípios existem para resolver problemas reais que enfrentamos durante o desenvolvimento de software, como a complexidade do código, a dificuldade de manutenção e a falta de clareza. Isso poder criar sistemas que são rígidos e que quebram com faclidade quando tentamos adicionar novas funcionalidades, gerando assim um sistema custoso e difícil de manter.

Quando aplicamos esses princípios de forma correta esses princípios, o código se torma mais **legível** (outros desenvolvedores conseguem entender o código facilmente), **flexível** (é fácil de adicionar novas funcionalidades sem quebrar o código existente) e **reutilizável** (é possível reutilizar partes do código em outros projetos), **testável** (é fácil de escrever testes automatizados para o código) e **manutenível** (é fácil de corrigir bugs e adicionar novas funcionalidades).

## A reutilização de código

**Custo** e **tempo**, esses são as duas maiores métricas ou parametros quando falamos de desenvolvimento de software. Isso ocorre porque no mundo atual grande parte das vantagens competitivas das empresas estão ligadas a tecnologia e a capacidade de desenvolver essa tecnologia de forma rápida e eficiente. Portanto, quanto mais rápido e eficiente for o desenvolvimento de software, maior será a vantagem competitiva da empresa.

A reutilização de código é uma das formas mais eficazes de reduzir o custo e o tempo de desenvolvimento de software. Quando reutilizamos código, estamos aproveitando o trabalho já feito, evitando a duplicação de esforços e reduzindo o tempo necessário para desenvolver novas funcionalidades.

A utilização de princípios de projetos de software é uma forma de tentar aumentar a flexibilidade dos componentes, tornando-os mais fáceis de serem reutilizados, contudo, isso pode gerar um código mais complexo e difícil de entender.

A reutilização de código pode ocorrer em diferentes "níveis", por assim dizer.

No nível mais **baixo**, temos a reutilização de classes, funções e métodos. Isso significa que podemos reutilizar partes do código em diferentes partes do mesmo projeto ou em projetos diferentes. Por exemplo, podemos ter uma classe que representa um cliente e reutilizá-la em diferentes partes do sistema, como na parte de cadastro de clientes, na parte de vendas, etc.

Num nível mais **intermediário** e abstrato, temos os padrões. Os padrões de projeto são mais abstratos que descrevem como uma receita que pode ser reutilizada em diferentes contextos.

**Aumentando** o nível de reaproveitamento, temos os frameworks. Os frameworks são conjuntos de bibliotecas e ferramentas que podem ser reutilizadas em diferentes projetos. Eles fornecem uma estrutura básica para o desenvolvimento de software, permitindo que os desenvolvedores se concentrem nas funcionalidades específicas do projeto, sem se preocupar com a infraestrutura básica. Porém são complexos de se construir e manter, e muitas vezes são utilizados como uma caixa preta, onde os desenvolvedores não têm controle total sobre o que está acontecendo por trás das cenas.

No nível mais **alto**, temos as plataformas. As plataformas são conjuntos de ferramentas e serviços que podem ser reutilizados em diferentes projetos. Elas fornecem uma infraestrutura completa para o desenvolvimento de software, permitindo que os desenvolvedores se concentrem apenas nas regras de negócio específicas do projeto. As plataformas são mais complexas que os frameworks e geralmente são utilizadas em projetos de grande escala.

## A extensibilidade do código

**Mudar**, por mais paradoxo que possa parecer, é uma constante no desenvolvimento de software. O software é uma tentativa de resolver um problema do mundo real, e o mundo real está sempre mudando. Portanto, o software também precisa mudar para se adaptar a essas mudanças.

Outro gatilho para a mudança é a experiência adquirida durante o desenvolvimento do software. À medida que os desenvolvedores trabalham no código, eles aprendem mais sobre o problema que estão tentando resolver e podem identificar melhorias e otimizações que podem ser feitas no código.

Dada essa realidade, é muito importante que o código tenha a capacidade de ser facilmente modificado e estendido para acomodar novos requisitos sem que seja preciso alterar significativamente o que já existe.

O código extensível geramente apresenta interfaces bem definidas que estabelecem contratos claros entre os diferentes componentes do sistema. Esse código também usa abstrações apropriadas para permitir diferentes implementações da mesma funcionalidade. Ele também tem baixo acoplamento entre os diferentes componentes do sistema, onde  mudanças em um componente não afetam outros componentes. Além disso, possuí alta coesão, onde cada componente tem uma única responsabilidade e é responsável por uma única funcionalidade do sistema.

O código extensível facilita a manutenção e a evolução do software, reduzindo o custo e o tempo de desenvolvimento, porém, é importante lembrar que o código extensível não deve ser confundido com o código complexo. A chave aqui é encontrar um equilíbrio entre a extensibilidade e a simplicidade do código. 

