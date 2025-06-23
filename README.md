# Hierarquia-de-Classes-ED-Lineares
A tarefa de programação orientada a objetos consiste em implementar uma hierarquia de classes de estruturas de dados lineares e resolver alguns dos problemas propostos.
from abc import ABC, abstractmethod

# Classe base abstrata para estruturas lineares
class EstruturaLinearBase(ABC):
    def __init__(self):
        self._tamanho = 0

    def tamanho(self):
        return self._tamanho

    def esta_vazia(self):
        return self._tamanho == 0

    @abstractmethod
    def remover_do_inicio(self):
        pass

    @abstractmethod
    def consultar_inicio(self):
        pass

# Implementação de Array Dinâmico usando lista Python
class VetorDinamico(EstruturaLinearBase):
    def __init__(self, dados=None):
        super().__init__()
        self._elementos = list(dados) if dados else []
        self._tamanho = len(self._elementos)

    def __getitem__(self, indice):
        if 0 <= indice < self._tamanho:
            return self._elementos[indice]
        else:
            raise IndexError("Índice fora do intervalo")

    def __setitem__(self, indice, valor):
        if 0 <= indice < self._tamanho:
            self._elementos[indice] = valor
        else:
            raise IndexError("Índice fora do intervalo")

    def adicionar_no_fim(self, valor):
        self._elementos.append(valor)
        self._tamanho += 1

    def adicionar_no_inicio(self, valor):
        self._elementos.insert(0, valor)
        self._tamanho += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("Vetor vazio")
        self._tamanho -= 1
        return self._elementos.pop(0)

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Vetor vazio")
        return self._elementos[0]

# Nó para lista encadeada simples
class NoSimples:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# Lista simplesmente encadeada
class ListaSimples(EstruturaLinearBase):
    def __init__(self):
        super().__init__()
        self.inicio = None

    def adicionar_no_inicio(self, valor):
        novo_no = NoSimples(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
        self._tamanho += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("Lista vazia")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        self._tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Lista vazia")
        return self.inicio.valor

    def acessar_por_indice(self, indice):
        if indice < 0 or indice >= self._tamanho:
            raise IndexError("Índice fora do intervalo")
        atual = self.inicio
        for _ in range(indice):
            atual = atual.proximo
        return atual.valor

# Nó para lista duplamente encadeada
class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

# Lista duplamente encadeada
class ListaDupla(EstruturaLinearBase):
    def __init__(self):
        super().__init__()
        self.inicio = None
        self.fim = None

    def adicionar_no_inicio(self, valor):
        novo_no = NoDuplo(valor)
        if self.inicio:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
        else:
            self.fim = novo_no
        self.inicio = novo_no
        self._tamanho += 1

    def adicionar_no_fim(self, valor):
        novo_no = NoDuplo(valor)
        if self.fim:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
        else:
            self.inicio = novo_no
        self.fim = novo_no
        self._tamanho += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("Lista vazia")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        self._tamanho -= 1
        return valor

    def remover_do_fim(self):
        if self.esta_vazia():
            raise IndexError("Lista vazia")
        valor = self.fim.valor
        self.fim = self.fim.anterior
        if self.fim:
            self.fim.proximo = None
        else:
            self.inicio = None
        self._tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Lista vazia")
        return self.inicio.valor

    def acessar_por_indice(self, indice):
        if indice < 0 or indice >= self._tamanho:
            raise IndexError("Índice fora do intervalo")
        atual = self.inicio
        for _ in range(indice):
            atual = atual.proximo
        return atual.valor

    def trocar_vizinhos(self, indice):
        if indice < 0 or indice >= self._tamanho - 1:
            raise IndexError("Índice inválido para troca")
        atual = self.inicio
        for _ in range(indice):
            atual = atual.proximo
        proximo = atual.proximo
        atual.valor, proximo.valor = proximo.valor, atual.valor

    def ordenar_bolha(self):
        if self._tamanho < 2:
            return
        trocou = True
        while trocou:
            trocou = False
            atual = self.inicio
            while atual.proximo:
                if atual.valor > atual.proximo.valor:
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                    trocou = True
                atual = atual.proximo

# Pilha implementada usando lista simplesmente encadeada
class Pilha(EstruturaLinearBase):
    def __init__(self):
        self._dados = ListaSimples()

    def adicionar_no_inicio(self, valor):
        self._dados.adicionar_no_inicio(valor)

    def remover_do_inicio(self):
        return self._dados.remover_do_inicio()

    def consultar_inicio(self):
        return self._dados.consultar_inicio()

    def tamanho(self):
        return self._dados.tamanho()

    def esta_vazia(self):
        return self._dados.esta_vazia()

# Fila simples implementada com nós simples
class Fila(EstruturaLinearBase):
    def __init__(self):
        super().__init__()
        self._frente = None
        self._fim = None

    def adicionar_no_fim(self, valor):
        novo_no = NoSimples(valor)
        if self._fim:
            self._fim.proximo = novo_no
        else:
            self._frente = novo_no
        self._fim = novo_no
        self._tamanho += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        valor = self._frente.valor
        self._frente = self._frente.proximo
        if not self._frente:
            self._fim = None
        self._tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        return self._frente.valor
