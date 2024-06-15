import numpy as np


class Fila:
    def __init__(self, capacidade):
        self.inicio = 0
        self.fim = -1
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
        
    def enfileirar(self, valor):
        if self.fila_cheia():
            print("Fila cheia")
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1
    
    def desenfileirar(self):
        if self.fila_vazia():
            print("Fila vazia")
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp