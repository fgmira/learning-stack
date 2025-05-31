# Relacionamentos entre classes

## Dependência

A *dependência* é um relacionamento temporário onde uma classe precisa de outra para executar uma ação específica, mas não matém uma referência permanente a ela.

### Características da Dependência:
- **Temporária**: a relação existe apenas durante a execução de um método.
- **Fraca**: mudanças na classe dependente não afetam a classe que depende dela, ou seja, a classe que depende não precisa conhecer os detalhes da implementação da classe dependente.
- **Transitória**: não existe uma duração duradoura entre os objetos envolvidos, a dependência é resolvida no momento da execução.

### Exemplo de Dependência:

1. Parâmetros de Método:
   ```python
   class Pedido:
       def gerar_relatorio(self, conexao: ConexaoBanco):
           # Usa a conexão para gerar um relatório
           conexao.executar_query("SELECT * FROM pedidos")
   ```
2. Variáveis Locais:
    ```python
    class Pedido:
        def processar(self):
            conexao = ConexaoBanco()  # Cria uma conexão temporária
            conexao.executar_query("UPDATE pedidos SET status='processado'")
    ```
3. Tipos de Retorno:
   ```python
   class Pedido:
       def obter_conexao(self) -> ConexaoBanco:
           return ConexaoBanco()  # Retorna uma conexão temporária
   ```

### O Problema da Dependência Forte:

Quando a classe depende de classes concretas, isso pode levar a um acoplamento forte, dificultando a manutenção e a testabilidade do código. 

```python
class NotificadorEmail:
    def enviar(self, mensagem: str):
        smtp = SmtpGmail()
        smtp.enviar_email(mensagem)
```
Para evitar isso, é recomendado o uso de interfaces ou classes abstratas, permitindo que a classe dependa de abstrações em vez de implementações concretas.

```python
from abc import ABC, abstractmethod

class NotificadorEmail:
    def enviar(self, mensagem: str, smtp: Smtp):
        smtp.enviar_email(mensagem)

class Smtp(ABC):
    @abstractmethod
    def enviar_email(self, mensagem: str):
        pass
```

## Associação

A *associação* é um relacionamento na qual uma classe usa ou interage com outra classe. A associação pode ser vista como um tipo especializado de dependência, onde uma classe sempre tem acesso às classes das quais ela interage.

A associação também pode ser definida como um relacionamento estrutural entre duas classes, onde uma classe contém uma referência a outra classe, permitindo que ocorra uma interação entre elas.

### Características da Associação:

- **Estrutural**: é um vinculo permanente entre duas classes, na qual mantém-se uma referência a outra classe, permitindo a navegação entre elas.
- **Independente**: as classes associadas podem existir independentemente uma da outra, ou seja, o ciclo de vida de uma classe não depende do ciclo de vida da outra, não existindo propriedade ou posse entre elas.

### Tipos de Associação:
1. **Associação Unidirecional**: uma classe conhece a outra, mas não o contrário.
   ```python
   class Cliente:
       def __init__(self, nome: str):
           self.nome = nome

   class Pedido:
       def __init__(self, cliente: Cliente):
           self.cliente = cliente  # Associação unidirecional
   ```
2. **Associação Bidirecional**: ambas as classes conhecem uma à outra.
   ```python
   class Cliente:
       def __init__(self, nome: str):
           self.nome = nome
           self.pedidos = []  # Lista de pedidos

       def adicionar_pedido(self, pedido):
           self.pedidos.append(pedido)
           pedido.cliente = self  # Associação bidirecional

   class Pedido:
         def __init__(self, descricao: str):
              self.descricao = descricao
              self.cliente: Cliente | None = None  # Referência ao cliente
    ```

### Quando Usar Associação:

#### Use quando:
- Quando objetos precisam colaborar mas são independentes
- Para modelar relacionamentos do mundo real que não envolvem propriedade
- Quando você quer flexibilidade para trocar objetos associados

#### Não use quando:
- Quando um objeto precisa controlar o ciclo de vida do outro (use composição)
- Quando um objeto precisa ser parte integrante do outro (use composição)

### Vantagens e Desvantagens da Associação:

#### Vantagens:
- **Flexibilidade**: permite que objetos sejam facilmente substituídos ou modificados
- **Baixo acoplamento**: objetos são independentes
- **Facilita manutenção**: mudanças em uma classe têm menor impacto
- **Testabilidade**: objetos podem ser testados separadamente

#### Desvantagens:
- **Complexidade**: pode tornar o design mais complexo
- **Dificuldade de rastreamento**: relacionamentos podem ser difíceis de seguir
- **Dependência implícita**: pode levar a dependências ocultas entre classes


## Agregação

A *agregação* é um tipo especial de associação que representa relações individuais (`one-to-many`), multipass (`many-to-many`) ou totais (`one-to-one`) entre classes, onde uma classe contém uma coleção de outras classes, mas não possui a responsabilidade de gerenciar o ciclo de vida dessas classes, ou seja, as classes podem existir independentemente da classe agregadora, não havendo posse ou propriedade entre elas (Acoplamento Fraco).

### Características da Agregação:

- **Relação "Tem Um" (Has-a)**: A classe "toda" comtém objetos "parte", representando uma coleção ou agrupamento e as partes mantêm uma identidade própria.
- **Independência das Partes**: As partes podem existir sem o todo, podendo pertencer a múltiplos "todos", onde destruir o todo não implica em destruir as partes.
- **Relacionamento mais forte que a associação**: A agregação implica em uma relação de contenção ou posse, sugindo uma responsabilidade do todo em relação às partes, mas sem propriedade exclusiva.

### Exemplo de Agregação:

```python
class Departamento:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []  # Lista de funcionários

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        funcionario.departamento = self  # Referência ao departamento
class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome
        self.departamento: Departamento | None = None  # Referência ao departamento
```

### Quando Usar Agregação:

#### Use quando:

- As partes podem existir sem o todo
- As partes podem pertencer a múltiplos "todos"
- Há uma relação clara de contenção, mas não de propriedade exclusiva
- Você quer modelar grupos, coleções ou conjuntos

#### Não use quando:

- As partes são criadas pelo todo (use composição)
- As partes não podem existir sem o todo (use composição)
- Não há relação de contenção (use associação simples)

### Vantagens e Desvantagens da Agregação:

#### Vantagens:

- **Reutilização**: partes podem ser compartilhadas
- **Flexibilidade**: fácil reorganização das partes
- **Manutenibilidade**: mudanças no todo não afetam diretamente as partes
- **Realismo**: modela bem relacionamentos do mundo real

#### Desvantagens:

- **Complexidade**: pode ser difícil de entender
- **Gerenciamento de Ciclo de Vida**: o todo não controla o ciclo de vida das partes
- **Acoplamento Fraco**: pode levar a problemas de consistência


## Composição

A *composição* é um tipo especial de agregação, onde um objeto é composto por um ou mais objetos, onde o todo **não pode existir sem as partes**. É uma forma especial de Agregação com propriedade exclusiva e dependência de cliclo de vida, ou seja, quando o todo é destruído, as partes também são destruídas. A composição é uma relação mais forte que a agregação.

### Características da Composição:

- **Propriedade Exclusiva**: O todo possui as partes, e as partes não podem existir sem o todo.
- **Ciclo de Vida Vinculado**: As partes são criada quando o todo é criado e destruídas quando o todo é destruído, ou seja, as partes não podem existir independentemente do todo.
- **Responsabilidade Total**: O todo é responsável por gerenciar o ciclo de vida das partes, ou seja, o todo controla a criação e destruição das partes

### Exemplo de Composição:

```python
class Carro:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.motor = Motor()  # O carro possui um motor
    def ligar(self):
        self.motor.ligar()  # O carro liga o motor
class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True  # O motor é ligado
```
### Quando Usar Composição

#### Use quando:

- As partes não fazem sentido sem o todo
- Você quer controle total sobre as partes
- As partes são específicas para aquele tipo de todo
- Há uma relação física ou conceitual forte

#### Não use quando:

- As partes podem existir independentemente
- As partes podem ser compartilhadas
- Você quer flexibilidade para trocar partes
- As partes são reutilizáveis em outros contextos

### Vantagens e Desvantages da Composição:

#### Vantagens:

- **Encapsulamento forte**: partes ficam completamente ocultas
- **Integridade**: garante que o objeto esteja sempre em estado válido
- **Simplicidade**: não precisa gerenciar partes externamente
- **Controle total**: responsabilidade clara sobre as partes

#### Desvantagens:

- **Rigidez**: difícil de modificar ou estender
- **Reutilização limitada**: partes não podem ser compartilhadas
- **Acoplamento forte**: mudanças nas partes afetam o todo

## Diferenças Importantes
|Aspecto|Agregação|Composição|Associação|
|---|---|---|---|
|**Relacionamento**|"Tem um"|"É composto de"|"Usa" ou "Conhece"|
|**Independência**|Partes independentes|Partes dependentes|Objetos independentes|
|**Propriedade**|Compartilhada|Exclusiva|Não há|
|**Ciclo de vida**|Independente|Dependente|Independente|
|**Controle**|Parcial|Total|Nenhum|
|**Força**|Média|Forte|Fraca|