# Introdução à Programação Orientada a Objetos (POO)

## O que é Programação Orientada a Objetos?

A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em **objetos** - entidades que combinam dados (atributos) e comportamentos (métodos). Em vez de pensar em funções que manipulam dados separadamente, a POO nos permite modelar o mundo real criando "coisas" digitais que se comportam de forma similar aos objetos reais.

Imagine um carro: ele tem características (cor, modelo, velocidade) e ações que pode realizar (acelerar, frear, ligar). Na POO, criamos uma representação digital desse carro com as mesmas propriedades e comportamentos.

## Breve História da POO

### Anos 1960 - Simula
- **Simula I (1962)** e **Simula 67 (1967)**: Desenvolvidas por Ole-Johan Dahl e Kristen Nygaard na Noruega
- Primeira linguagem a introduzir conceitos de classes e objetos
- Criada inicialmente para simulações, daí o nome "Simula"
- Estabeleceu as bases conceituais da POO

### Anos 1970 - Smalltalk
- **Smalltalk (1972)**: Desenvolvida por Alan Kay na Xerox PARC
- Primeira linguagem puramente orientada a objetos
- Criou o termo "programação orientada a objetos"
- Introduziu conceitos como herança, polimorfismo e envio de mensagens

### Anos 1980-1990 - Popularização
- **C++ (1983)**: Bjarne Stroustrup adiciona POO ao C
- **Objective-C (1984)**: Combina C com conceitos do Smalltalk
- **Java (1995)**: Sun Microsystems populariza POO massivamente
- **Python (1991)**: Guido van Rossum cria Python com suporte natural à POO

## Conceitos Fundamentais da POO

### 1. Classe
Uma **classe** é um modelo ou template que define como os objetos serão criados. É como uma "forma de bolo" que determina a estrutura e comportamento dos objetos.

```python
class Pessoa:
    # Atributos da classe (compartilhados por todas as instâncias)
    especie = "Homo sapiens"
    
    # Método construtor
    def __init__(self, nome, idade, cpf):
        # Atributos de instância (específicos de cada objeto)
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Convenção para "privado"
    
    # Métodos (comportamentos)
    def falar(self):
        print(f"{self.nome} está falando")
    
    def andar(self):
        print(f"{self.nome} está andando")
    
    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos")
```

### 2. Objeto
Um **objeto** é uma instância de uma classe - uma "cópia" criada a partir do modelo da classe, com valores específicos para seus atributos.

```python
# Criando objetos da classe Pessoa
joao = Pessoa("João Silva", 30, "123.456.789-00")
maria = Pessoa("Maria Santos", 25, "987.654.321-00")

# Acessando atributos
print(joao.nome)  # João Silva
print(maria.idade)  # 25

# Chamando métodos
joao.falar()  # João Silva está falando
maria.andar()  # Maria Santos está andando
```

### 3. Atributos (Propriedades)
**Atributos** são as características ou dados que descrevem um objeto. Em Python, temos diferentes tipos de atributos.

```python
class Carro:
    # Atributo de classe (compartilhado por todos os carros)
    rodas = 4
    
    def __init__(self, marca, modelo, ano):
        # Atributos de instância (específicos de cada carro)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self._combustivel = 50  # "Privado" por convenção
        self.__numero_chassi = "ABC123"  # "Muito privado"
    
    @property
    def combustivel(self):
        """Getter para combustível"""
        return self._combustivel
    
    @combustivel.setter
    def combustivel(self, valor):
        """Setter para combustível com validação"""
        if 0 <= valor <= 100:
            self._combustivel = valor
        else:
            print("Combustível deve estar entre 0 e 100")
```

### 4. Métodos (Comportamentos)
**Métodos** são as ações que um objeto pode realizar. Em Python, temos diferentes tipos de métodos.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    
    # Método de instância
    def acelerar(self, incremento=10):
        self.velocidade += incremento
        print(f"{self.marca} {self.modelo} acelerou para {self.velocidade} km/h")
    
    def frear(self, decremento=10):
        self.velocidade = max(0, self.velocidade - decremento)
        print(f"{self.marca} {self.modelo} freou para {self.velocidade} km/h")
    
    # Método estático (não acessa self ou cls)
    @staticmethod
    def calcular_consumo(distancia, litros):
        return distancia / litros if litros > 0 else 0
    
    # Método de classe (acessa cls, não self)
    @classmethod
    def criar_carro_popular(cls, marca):
        return cls(marca, "Hatch")
    
    # Método especial (dunder method)
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.velocidade} km/h"
```

## Os Quatro Pilares da POO

### 1. Encapsulamento

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # "Privado" por convenção
        self.__historico = []  # "Muito privado"
    
    @property
    def saldo(self):
        """Getter para saldo - só leitura"""
        return self._saldo
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.__historico.append(f"Depósito: +R$ {valor}")
            print(f"Depósito realizado. Saldo atual: R$ {self._saldo}")
        else:
            print("Valor deve ser positivo")
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            self.__historico.append(f"Saque: -R$ {valor}")
            print(f"Saque realizado. Saldo atual: R$ {self._saldo}")
        else:
            print("Saldo insuficiente ou valor inválido")
    
    def _extrato_simples(self):
        """Método 'protegido' - uso interno"""
        return self.__historico[-5:]  # Últimas 5 transações

# Uso
conta = ContaBancaria("João", 1000)
print(conta.saldo)  # 1000 (getter)
conta.depositar(500)  # Depósito realizado. Saldo atual: R$ 1500
# conta.saldo = 2000  # Erro! Não tem setter
```

### 2. Herança

```python
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.energia = 100
    
    def comer(self):
        self.energia += 10
        print(f"{self.nome} está comendo. Energia: {self.energia}")
    
    def dormir(self):
        self.energia += 20
        print(f"{self.nome} está dormindo. Energia: {self.energia}")
    
    def __str__(self):
        return f"{self.nome} ({self.especie})"

class Mamifero(Animal):
    def __init__(self, nome, especie, pelos=True):
        super().__init__(nome, especie)  # Chama construtor da classe pai
        self.pelos = pelos
    
    def amamentar(self):
        print(f"{self.nome} está amamentando")

class Cachorro(Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome, "Canis lupus", pelos=True)
        self.raca = raca
    
    def latir(self):
        self.energia -= 5
        print(f"{self.nome} está latindo: Au au!")
    
    def comer(self):  # Sobrescrevendo método da classe pai
        super().comer()  # Chama método original
        print(f"{self.nome} balança o rabo de felicidade!")

# Uso
rex = Cachorro("Rex", "Labrador")
rex.comer()    # Rex está comendo. Energia: 110
               # Rex balança o rabo de felicidade!
rex.latir()    # Rex está latindo: Au au!
rex.dormir()   # Rex está dormindo. Energia: 125
```

### 3. Polimorfismo

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def emitir_som(self):
        pass
    
    def apresentar(self):
        print(f"Eu sou {self.nome}")
        self.emitir_som()

class Gato(Animal):
    def emitir_som(self):
        print("Miau miau!")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au au!")

class Pato(Animal):
    def emitir_som(self):
        print("Quack quack!")

# Polimorfismo em ação
def fazer_barulho(animais):
    for animal in animais:
        animal.apresentar()  # Mesmo método, comportamentos diferentes
        print("-" * 20)

# Uso
animais = [
    Gato("Mimi"),
    Cachorro("Bolt"),
    Pato("Donald")
]

fazer_barulho(animais)
# Eu sou Mimi
# Miau miau!
# --------------------
# Eu sou Bolt
# Au au au!
# --------------------
# Eu sou Donald
# Quack quack!
```

### 4. Abstração

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
    
    @abstractmethod
    def acelerar(self):
        """Método abstrato - deve ser implementado pelas classes filhas"""
        pass
    
    @abstractmethod
    def frear(self):
        """Método abstrato - deve ser implementado pelas classes filhas"""
        pass
    
    # Método concreto - comum a todos os veículos
    def ligar(self):
        self._ligado = True
        print(f"{self.marca} {self.modelo} ligado")
    
    def desligar(self):
        self._ligado = False
        print(f"{self.marca} {self.modelo} desligado")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
        self.velocidade = 0
    
    def acelerar(self):
        if self._ligado:
            self.velocidade += 10
            print(f"Carro acelerando: {self.velocidade} km/h")
        else:
            print("Ligue o carro primeiro!")
    
    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        print(f"Carro freando: {self.velocidade} km/h")

class Moto(Veiculo):
    def acelerar(self):
        if self._ligado:
            print("Moto acelerando rapidamente!")
        else:
            print("Ligue a moto primeiro!")
    
    def frear(self):
        print("Moto freando!")

# Uso
carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CB600")

carro.ligar()      # Toyota Corolla ligado
carro.acelerar()   # Carro acelerando: 10 km/h
moto.ligar()       # Honda CB600 ligado
moto.acelerar()    # Moto acelerando rapidamente!
```

## Características Especiais da POO em Python

### 1. Duck Typing
"Se anda como um pato e faz quack como um pato, então é um pato"

```python
class Pato:
    def nadar(self):
        print("Pato nadando")
    
    def voar(self):
        print("Pato voando")

class Pessoa:
    def nadar(self):
        print("Pessoa nadando")
    
    def voar(self):
        print("Pessoa voando de avião")

def atividades_aquaticas(ser):
    ser.nadar()  # Não importa o tipo, só precisa ter o método nadar()
    ser.voar()

pato = Pato()
pessoa = Pessoa()

atividades_aquaticas(pato)    # Pato nadando / Pato voando
atividades_aquaticas(pessoa)  # Pessoa nadando / Pessoa voando de avião
```

### 2. Métodos Especiais (Dunder Methods)

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
    
    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"
    
    def __eq__(self, other):
        return self.nome == other.nome and self.preco == other.preco
    
    def __lt__(self, other):
        return self.preco < other.preco
    
    def __add__(self, other):
        return self.preco + other.preco

# Uso
produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Mouse", 50.00)

print(produto1)           # Notebook - R$ 2500.0
print(repr(produto2))     # Produto('Mouse', 50.0)
print(produto1 < produto2)  # False
print(produto1 + produto2)  # 2550.0
```

### 3. Properties e Decoradores

```python
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura não pode ser menor que -273.15°C")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

# Uso
temp = Temperatura(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
print(temp.kelvin)      # 298.15

temp.fahrenheit = 100
print(temp.celsius)     # 37.77777777777778
```

## Vantagens da POO em Python

### **Simplicidade e Legibilidade**
Python torna a POO mais acessível com sintaxe clara e natural.

### **Flexibilidade**
Duck typing permite polimorfismo sem hierarquias rígidas.

### **Introspecção**
Python permite examinar objetos em tempo de execução.

### **Múltipla Herança**
Suporte nativo à herança múltipla com MRO (Method Resolution Order).

## Exemplo Prático Completo

```python
class Funcionario:
    # Atributo de classe
    empresa = "TechCorp"
    
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self._salario = salario
        self.cargo = cargo
        self._historico_salarios = [salario]
    
    @property
    def salario(self):
        return self._salario
    
    def trabalhar(self):
        print(f"{self.nome} está trabalhando como {self.cargo}")
    
    def receber_aumento(self, percentual):
        if percentual > 0:
            novo_salario = self._salario * (1 + percentual / 100)
            self._salario = novo_salario
            self._historico_salarios.append(novo_salario)
            print(f"{self.nome} recebeu aumento de {percentual}%")
            print(f"Novo salário: R$ {self._salario:.2f}")
        else:
            print("Percentual deve ser positivo")
    
    def __str__(self):
        return f"{self.nome} - {self.cargo} - R$ {self._salario:.2f}"
    
    def __repr__(self):
        return f"Funcionario('{self.nome}', {self._salario}, '{self.cargo}')"

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagens=None):
        super().__init__(nome, salario, "Desenvolvedor")
        self.linguagens = linguagens or []
    
    def programar(self, linguagem):
        if linguagem in self.linguagens:
            print(f"{self.nome} está programando em {linguagem}")
        else:
            print(f"{self.nome} não conhece {linguagem}")
            self.aprender_linguagem(linguagem)
    
    def aprender_linguagem(self, linguagem):
        self.linguagens.append(linguagem)
        print(f"{self.nome} aprendeu {linguagem}!")

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe=None):
        super().__init__(nome, salario, "Gerente")
        self.equipe = equipe or []
    
    def adicionar_funcionario(self, funcionario):
        self.equipe.append(funcionario)
        print(f"{funcionario.nome} foi adicionado à equipe de {self.nome}")
    
    def reuniao_equipe(self):
        print(f"{self.nome} está conduzindo reunião com:")
        for funcionario in self.equipe:
            print(f"  - {funcionario.nome}")

# Usando as classes
def main():
    # Criando funcionários
    dev1 = Desenvolvedor("Ana Silva", 8000, ["Python", "JavaScript"])
    dev2 = Desenvolvedor("Carlos Santos", 7500, ["Java", "Python"])
    gerente = Gerente("Maria Oliveira", 12000)
    
    # Montando equipe
    gerente.adicionar_funcionario(dev1)
    gerente.adicionar_funcionario(dev2)
    
    # Simulando trabalho
    print("\n=== Dia de trabalho ===")
    dev1.trabalhar()
    dev1.programar("Python")
    dev1.programar("Go")  # Vai aprender
    
    dev2.trabalhar()
    dev2.programar("Java")
    
    gerente.trabalhar()
    gerente.reuniao_equipe()
    
    # Aumentos
    print("\n=== Avaliação anual ===")
    dev1.receber_aumento(10)
    dev2.receber_aumento(8)
    gerente.receber_aumento(15)
    
    # Status final
    print("\n=== Status da equipe ===")
    print(dev1)
    print(dev2)
    print(gerente)

if __name__ == "__main__":
    main()
```

## Quando Usar POO?

### **✅ Ideal para:**
- Sistemas complexos com muitas entidades
- Aplicações que modelam o mundo real
- Projetos que precisam de manutenção constante
- Desenvolvimento em equipe
- Sistemas que precisam ser extensíveis

### **❌ Pode não ser a melhor escolha para:**
- Scripts simples e pequenos
- Cálculos matemáticos intensivos
- Programação de sistemas de baixo nível
- Aplicações com restrições severas de performance

## Conclusão

A Programação Orientada a Objetos revolucionou o desenvolvimento de software ao permitir que organizemos código de forma mais natural e intuitiva. Seus conceitos fundamentais - classes, objetos, encapsulamento, herança, polimorfismo e abstração - fornecem ferramentas poderosas para criar sistemas complexos e maintível.

Embora possa parecer complexa no início, a POO torna-se natural com a prática. O segredo é começar pequeno, entender bem os conceitos básicos e gradualmente aplicá-los em projetos mais complexos.

A POO não é apenas uma forma de programar - é uma maneira de pensar sobre problemas e soluções de software que continua relevante e poderosa décadas após sua criação.

Específicamente o Python torna a Programação Orientada a Objetos mais acessível e poderosa, mantendo a simplicidade que caracteriza a linguagem. Com recursos como duck typing, properties, métodos especiais e herança múltipla, Python oferece todas as ferramentas necessárias para criar sistemas robustos e elegantes.

A filosofia "pythônica" se aplica também à POO: prefira clareza sobre cleverness[^1], use convenções em vez de imposições rígidas, e sempre busque a solução mais simples que funciona.

Lembre-se: em Python, nem tudo precisa ser uma classe. Use POO quando ela realmente agregar valor ao seu código, tornando-o mais organizado, reutilizável e fácil de manter.

[^1]: Quando falamos de cleverness em código, estamos nos referindo a:
    
    Código "Esperto" Demais
    - Soluções excessivamente complexas ou obscuras
    - Truques de programação difíceis de entender
    - Otimizações prematuras que sacrificam legibilidade
    - Uso de recursos avançados da linguagem desnecessariamente

    Exemplo de Cleverness (RUIM):
    
    ```python
    # Código "cleverness" - difícil de entender
    result = [x for x in range(100) if all(x % i for i in range(2, int(x**0.5) + 1)) and x > 1]
    ```
    
    Código Claro (BOM):
    
    ```python
    # Código claro - fácil de entender
    def eh_primo(numero):
        if numero < 2:
            return False
        
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    numeros_primos = []
    for numero in range(2, 100):
        if eh_primo(numero):
            numeros_primos.append(numero)
    ```
