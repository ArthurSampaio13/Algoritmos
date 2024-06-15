import numpy as np

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostra_no(self):
    print(self.valor)
    
class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def insere_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def mostrar(self):
    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo

  def excluir_inicio(self):
    if self.primeiro == None:
      print('Lista vazia')
      return None

    temp = self.primeiro

    self.primeiro = self.primeiro.proximo
    return temp

  def pesquisa(self, valor):
    if self.primeiro == None:
      print('Lista vazia')
      return None

    atual = self.primeiro

    while atual.valor != valor:
      if atual.proximo == None:
        print("elemento nao encontrado")
        return None

      else:
        atual = atual.proximo
    return atual

  def excluir(self, valor):
    if self.primeiro == None:
      print('Lista vazia')
      return None

    atual = self.primeiro
    anterior = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        return None
      else:
        anterior = atual
        atual = atual.proximo

    if atual == self.primeiro:
      self.primeiro = self.primeiro.proximo
    else:
      anterior.proximo = atual.proximo
    return atual
  
  def inverter(self):
    anterior = None
    atual = self.primeiro
    while atual is not None:
      proximo = atual.proximo
      atual.proximo = anterior
      anterior = atual
      atual = proximo
    self.primeiro = anterior

if __name__ == '__main__':
  a = ListaEncadeada()
  a.insere_inicio(1)
  a.insere_inicio(2)
  a.insere_inicio(3)
  a.mostrar()
  a.inverter()
  a.mostrar()
  