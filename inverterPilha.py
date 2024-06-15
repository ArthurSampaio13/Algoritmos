import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.topo = -1
        self.capacidade = capacidade
        self.valores = np.empty(self.capacidade, dtype=int)

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1
    
    def pilha_vazia(self):
        return self.topo == -1
            
    def empilhar(self, valor):
        if self.pilha_cheia():
            print("Pilha cheia")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha vazia")
            return None
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor
    
    def inverter(self):
        temp = Pilha(self.capacidade)
        while not self.pilha_vazia():
            temp.empilhar(self.desempilhar())
        self.valores = temp.valores
        self.topo = temp.topo
                  
    def __str__(self):
        return str(self.valores[:self.topo + 1])
                  
if __name__ == '__main__':
    pilha = Pilha(5)
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    print("Pilha antes de inverter:", pilha.valores[:pilha.topo+1])
    pilha.inverter()
    print("Pilha depois de inverter:", pilha.valores[:pilha.topo+1])