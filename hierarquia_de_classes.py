from abc import ABC, abstractmethod

# ----------------------
# Classe abstrata base
# ----------------------
class EstruturaLinear(ABC):
    def __init__(self):
        self._tamanho = 0

    def comprimento(self):
        return self._tamanho

    def esta_vazia(self):
        return self._tamanho == 0

    @abstractmethod
    def remover_inicio(self): pass

    @abstractmethod
    def consultar_inicio(self): pass

# ----------------------
# Array
# ----------------------
class Array(EstruturaLinear):
    def __init__(self, iterable=None):
        super().__init__()
        self._dados = list(iterable) if iterable else []
        self._tamanho = len(self._dados)

    def __getitem__(self, index):
        if 0 <= index < self._tamanho:
            return self._dados[index]
        raise IndexError("Índice fora do limite.")

    def __setitem__(self, index, value):
        if 0 <= index < self._tamanho:
            self._dados[index] = value
        else:
            raise IndexError("Índice fora do limite.")

    def inserir_fim(self, item):
        self._dados.append(item)
        self._tamanho += 1

    def inserir_inicio(self, item):
        self._dados.insert(0, item)
        self._tamanho += 1

    def remover_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        self._tamanho -= 1
        return self._dados.pop(0)

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        return self._dados[0]

# ----------------------
# Lista encadeada simples
# ----------------------
class NoSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaSimples(EstruturaLinear):
    def __init__(self):
        super().__init__()
        self.inicio = None

    def inserir_inicio(self, item):
        novo = NoSimples(item)
        novo.proximo = self.inicio
        self.inicio = novo
        self._tamanho += 1

    def remover_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        valor = self.inicio.dado
        self.inicio = self.inicio.proximo
        self._tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        return self.inicio.dado

    def consultar_na_posicao(self, pos):
        if pos < 0 or pos >= self._tamanho:
            raise IndexError("Posição inválida")
        atual = self.inicio
        for _ in range(pos):
            atual = atual.proximo
        return atual.dado

# ----------------------
# Lista duplamente encadeada
# ----------------------
class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada(EstruturaLinear):
    def __init__(self):
        super().__init__()
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, item):
        novo = NoDuplo(item)
        if self.inicio:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
        else:
            self.fim = novo
        self.inicio = novo
        self._tamanho += 1

    def inserir_fim(self, item):
        novo = NoDuplo(item)
        if self.fim:
            self.fim.proximo = novo
            novo.anterior = self.fim
        else:
            self.inicio = novo
        self.fim = novo
        self._tamanho += 1

    def remover_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        valor = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        self._tamanho -= 1
        return valor

    def remover_fim(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        valor = self.fim.dado
        self.fim = self.fim.anterior
        if self.fim:
            self.fim.proximo = None
        else:
            self.inicio = None
        self._tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        return self.inicio.dado

    def consultar_na_posicao(self, pos):
        if pos < 0 or pos >= self._tamanho:
            raise IndexError("Índice inválido")
        atual = self.inicio
        for _ in range(pos):
            atual = atual.proximo
        return atual.dado

    def swap(self, i):
        if i < 0 or i >= self._tamanho - 1:
            raise IndexError("Índice inválido para troca")
        atual = self.inicio
        for _ in range(i):
            atual = atual.proximo
        proximo = atual.proximo
        atual.dado, proximo.dado = proximo.dado, atual.dado

    def bubble_sort(self):
        if self._tamanho < 2:
            return
        trocado = True
        while trocado:
            trocado = False
            atual = self.inicio
            while atual.proximo:
                if atual.dado > atual.proximo.dado:
                    atual.dado, atual.proximo.dado = atual.proximo.dado, atual.dado
                    trocado = True
                atual = atual.proximo

# ----------------------
# Pilha com lista encadeada
# ----------------------
class Pilha(EstruturaLinear):
    def __init__(self):
        self._dados = ListaEncadeadaSimples()

    def inserir_inicio(self, item):
        self._dados.inserir_inicio(item)

    def remover_inicio(self):
        return self._dados.remover_inicio()

    def consultar_inicio(self):
        return self._dados.consultar_inicio()

    def comprimento(self):
        return self._dados.comprimento()

    def esta_vazia(self):
        return self._dados.esta_vazia()

# ----------------------
# Fila simples (Queue)
# ----------------------
class FilaSimples(EstruturaLinear):
    def __init__(self):
        super().__init__()
        self.inicio = None
        self.fim = None

    def inserir_fim(self, item):
        novo = NoSimples(item)
        if self.fim:
            self.fim.proximo = novo
        else:
            self.inicio = novo
        self.fim = novo
        self._tamanho += 1

    def remover_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        valor = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self._tamanho -= 1
        return valor

    def consultar_inicio(self):
        if self.esta_vazia():
            raise IndexError("Underflow")
        return self.inicio.dado
