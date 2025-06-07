# Design Patterns Criacionais - Resumo Comparativo

## Visão Geral

Os **Design Patterns Criacionais** fornecem diferentes mecanismos para criar objetos, aumentando a flexibilidade e reutilização do código. Estudamos cinco padrões fundamentais, cada um resolvendo problemas específicos de criação de objetos.

## Os Cinco Padrões Criacionais

### 1. Factory Method
**Objetivo**: Criar objetos sem especificar suas classes exatas, delegando a criação para subclasses.

**Problema que resolve**: Acoplamento forte entre código cliente e classes concretas.

**Exemplo**: Sistema de processamento de documentos (PDF, Word, Excel).

### 2. Abstract Factory  
**Objetivo**: Criar famílias de objetos relacionados sem especificar suas classes concretas.

**Problema que resolve**: Inconsistência entre produtos que devem trabalhar juntos.

**Exemplo**: Interface gráfica multiplataforma (Windows, Mac, Linux).

### 3. Builder
**Objetivo**: Construir objetos complexos passo a passo, permitindo diferentes representações.

**Problema que resolve**: Construtores telescópicos e objetos com muitos parâmetros opcionais.

**Exemplo**: Configuração de computadores com múltiplas opções.

### 4. Prototype
**Objetivo**: Criar objetos clonando instâncias existentes em vez de construir do zero.

**Problema que resolve**: Criação custosa de objetos com configurações complexas.

**Exemplo**: Editor gráfico com formas complexas e efeitos.

### 5. Singleton
**Objetivo**: Garantir que uma classe tenha apenas uma instância com acesso global.

**Problema que resolve**: Múltiplas instâncias de recursos que devem ser únicos.

**Exemplo**: Sistema de logging e configuração corporativo.

## Quadro Comparativo Detalhado

| Aspecto | Factory Method | Abstract Factory | Builder | Prototype | Singleton |
|---------|----------------|------------------|---------|-----------|-----------|
| **Foco Principal** | Como criar UM objeto | Quais objetos criar juntos | Como configurar objeto complexo | Como duplicar objeto existente | Como garantir instância única |
| **Número de Produtos** | 1 tipo | Múltiplos tipos relacionados | 1 tipo complexo | 1 tipo (clonado) | 1 instância global |
| **Complexidade** | Baixa | Média-Alta | Média | Baixa-Média | Baixa |
| **Flexibilidade** | Alta para extensões | Alta para famílias | Alta para configurações | Baixa | Muito Baixa |
| **Performance** | Normal | Normal | Normal | Alta (clonagem) | Normal |
| **Uso de Herança** | Sim (subclasses) | Não (composição) | Não | Não | Não |
| **Thread Safety** | Não é concern | Não é concern | Depende implementação | Cuidado com referências | Crítico |
| **Testabilidade** | Boa | Boa | Boa | Boa | Ruim |

## Quando Usar Cada Padrão

### Factory Method - Use quando:
- Você tem diferentes implementações da mesma interface
- Precisa delegar criação para subclasses
- Quer desacoplar criação do uso
- Planeja adicionar novos tipos frequentemente

**Não use quando:**
- Você tem apenas uma implementação
- A criação é trivial
- Não há previsão de extensibilidade

### Abstract Factory - Use quando:
- Precisa criar famílias de produtos relacionados
- Tem múltiplas plataformas/variantes
- Produtos devem ser compatíveis entre si
- Quer trocar famílias inteiras facilmente

**Não use quando:**
- Tem poucos produtos relacionados
- Produtos não precisam ser compatíveis
- Apenas uma família existe

### Builder - Use quando:
- Objeto tem muitos parâmetros (4+)
- Muitos parâmetros são opcionais
- Construção requer validação complexa
- Quer criar diferentes representações

**Não use quando:**
- Objeto tem poucos parâmetros simples
- Criação é direta e simples
- Não há lógica de validação especial

### Prototype - Use quando:
- Criação de objeto é custosa
- Objetos têm configurações complexas
- Precisa criar muitas variações similares
- Tipos são determinados em runtime

**Não use quando:**
- Criação é rápida e simples
- Objetos são únicos/diferentes
- Tem problemas com referências circulares

### Singleton - Use quando:
- Recurso deve ser único por natureza
- Precisa de acesso global controlado
- Estado deve ser compartilhado globalmente
- Inicialização é custosa

**Não use quando:**
- Testabilidade é crítica
- Sistema é complexo/grande
- Múltiplas configurações são necessárias


## Combinações de Padrões

### Padrões que se Complementam

1. **Abstract Factory + Factory Method**
   - Abstract Factory usa Factory Methods para criar cada produto
   - Exemplo: UIFactory usa createButton(), createWindow() methods

2. **Builder + Factory Method**
   - Factory Method retorna Builder apropriado
   - Exemplo: DocumentBuilderFactory.getBuilder(type)

3. **Prototype + Factory Method**
   - Factory Method retorna clones de protótipos
   - Exemplo: ShapeFactory usando registry de protótipos

4. **Singleton + Factory Method**
   - Singleton gerencia factories
   - Exemplo: FactoryManager singleton

### Padrões que se Conflitam

1. **Singleton vs Dependency Injection**
   - Filosofias opostas sobre gerenciamento de dependências
   - DI é preferível em sistemas modernos

2. **Factory Method vs Direct Instantiation**
   - Over-engineering vs simplicidade
   - Use factory apenas quando necessário

## Diretrizes de Escolha

### Fluxograma de Decisão

```
Precisa criar objetos?
├─ Apenas um tipo de objeto?
│  ├─ Muitos parâmetros opcionais? → Builder
│  ├─ Criação custosa? → Prototype  
│  ├─ Deve ser único? → Singleton
│  └─ Diferentes implementações? → Factory Method
└─ Múltiplos tipos relacionados? → Abstract Factory
```

### Perguntas para Guiar a Escolha

1. **Quantos tipos de objetos diferentes preciso criar?**
   - Um tipo → Factory Method, Builder, Prototype, Singleton
   - Múltiplos tipos → Abstract Factory

2. **A criação é complexa ou custosa?**
   - Complexa (muitos parâmetros) → Builder
   - Custosa (recursos, I/O) → Prototype

3. **Preciso de múltiplas instâncias?**
   - Não, deve ser único → Singleton
   - Sim, múltiplas instâncias → outros padrões

4. **Produtos devem ser compatíveis entre si?**
   - Sim, famílias compatíveis → Abstract Factory
   - Não, produtos independentes → Factory Method

5. **Quão frequentemente novos tipos serão adicionados?**
   - Frequentemente → Factory Method, Abstract Factory
   - Raramente → Builder, Prototype

## Anti-Patterns e Armadilhas Comuns

### Factory Method
- **Over-engineering**: Usar para criação simples
- **Subclasses desnecessárias**: Criar hierarquia só para factory
- **Acoplamento temporal**: Dependência da ordem de criação

### Abstract Factory
- **Explosão de classes**: Muitas factories para poucas variações
- **Rigidez**: Dificultar adição de novos produtos
- **Complexidade excessiva**: Usar para produtos não relacionados

### Builder
- **Builder desnecessário**: Para objetos simples
- **Validação inadequada**: Não validar estado durante construção
- **Interface confusa**: Muitos métodos opcionais sem clareza

### Prototype
- **Clone inadequado**: Problemas com deep vs shallow copy
- **Referências circulares**: Loops infinitos em clonagem
- **Estado mutável compartilhado**: Efeitos colaterais indesejados

### Singleton
- **Global state**: Estado global dificulta testes
- **Hidden dependencies**: Dependências não explícitas
- **Thread safety**: Problemas de concorrência

## Tendências Modernas

### Padrões em Ascensão
- **Dependency Injection**: Substitui muitos usos de Singleton
- **Functional Factories**: Funções em vez de classes
- **Immutable Objects**: Combinado com Builder pattern

### Padrões em Declínio
- **Singleton**: Considerado anti-pattern por muitos
- **Abstract Factory complexas**: Preferência por composição simples

### Influência de Linguagens Modernas
- **Python**: Factory functions são mais pythônicas
- **JavaScript**: Module pattern como singleton natural
- **Go**: Interfaces pequenas reduzem necessidade de factories

## Conclusões e Recomendações

### Princípios Gerais

1. **Simplicidade primeiro**: Use o padrão mais simples que resolve o problema
2. **YAGNI (You Ain't Gonna Need It)**: Não antecipe necessidades futuras
3. **Preferir composição**: Combine padrões simples em vez de um complexo
4. **Testabilidade**: Considere impacto nos testes desde o início

### Ordem de Preferência (Geral)

1. **Factory Method**: Mais simples e flexível
2. **Builder**: Excelente para objetos complexos
3. **Abstract Factory**: Para famílias bem definidas
4. **Prototype**: Para casos específicos de performance
5. **Singleton**: Use com extrema cautela

### Checklist de Aplicação

Antes de aplicar um padrão criacional, verifique:

- [ ] O problema realmente existe?
- [ ] A solução simples não atende?
- [ ] O padrão escolhido é o mais apropriado?
- [ ] A implementação será testável?
- [ ] A equipe entende o padrão?
- [ ] O benefício supera a complexidade?

### Palavras Finais

Os **Design Patterns Criacionais** são ferramentas poderosas quando aplicados nos contextos corretos. Eles promovem flexibilidade, reutilização e manutenibilidade, mas também podem introduzir complexidade desnecessária se mal utilizados.

A chave do sucesso está em:
- **Entender profundamente** cada padrão
- **Reconhecer os problemas** que cada um resolve
- **Aplicar com moderação** e sempre considerando alternativas mais simples
- **Manter o foco** na solução do problema real, não na elegância do padrão

Lembre-se: **padrões são soluções para problemas recorrentes, não soluções em busca de problemas**.