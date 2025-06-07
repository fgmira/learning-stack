# A Classificação dos Design Patterns

De acordo com o livro [**"Padrões de Projeto – Soluções Reutilizáveis de Software Orientado a Objetos"**](https://www.amazon.com.br/Padr%C3%B5es-Projetos-Solu%C3%A7%C3%B5es-Reutiliz%C3%A1veis-Orientados/dp/8573076100) da **Gang of Four**, existem três classificações de Design Patterns:

## Padrões de Criação

Os padrões de criação abstraem e/ou adiam o processo de criação dos objetos. Eles ajudam a tornar um sistema independente de como seus objetos são criados, compostos e representados. 

Um padrão de criação de classe usa herança para variar a classe instanciada, enquanto um padrão de criação de objeto delega a instanciação para outro objeto. Os padrões de criação tornam-se importantes à medida que os sistemas evoluem para depender mais da composição de objetos do que da herança de classes.

O desenvolvimento baseado na composição de objetos possibilita que os objetos sejam compostos sem expor seu interior, como acontece na herança de classe. Isso permite definir comportamentos dinamicamente, deslocando a ênfase da codificação rígida de comportamentos fixos para a definição de comportamentos menores que podem ser compostos para criar funcionalidades mais complexas.

**Dois temas principais caracterizam esses padrões:**

1. **Encapsulamento**: Todos encapsulam conhecimento sobre quais classes concretas são usadas pelo sistema
2. **Ocultação**: Ocultam como essas classes são criadas e montadas. O sistema conhece apenas as classes abstratas que definem os objetos

Consequentemente, os padrões de criação oferecem grande flexibilidade no que é criado, quem cria, como e quando é criado. Permitem configurar um sistema com objetos "produto" que variam amplamente em estrutura e funcionalidade. A configuração pode ser estática (especificada em tempo de compilação) ou dinâmica (em tempo de execução).

## Padrões Estruturais

Os padrões estruturais se preocupam com a forma como classes e objetos são compostos para formar estruturas maiores. Os padrões de classes utilizam herança para compor interfaces ou implementações, enquanto os padrões de objeto descrevem maneiras de compor objetos para obter novas funcionalidades.

A flexibilidade obtida pela composição de objetos provém da capacidade de mudar a composição em tempo de execução, o que não é possível com a composição estática (herança de classes).

## Padrões Comportamentais

Os padrões comportamentais se concentram nos algoritmos e na atribuição de responsabilidades entre objetos. Eles não descrevem apenas padrões de objetos ou classes, mas também os padrões de comunicação entre eles.

Os padrões comportamentais de classes utilizam herança para distribuir comportamento entre classes, enquanto os padrões comportamentais de objeto utilizam composição de objetos em contrapartida à herança. Alguns descrevem como grupos de objetos cooperam para executar tarefas que não poderiam ser realizadas por um objeto sozinho.