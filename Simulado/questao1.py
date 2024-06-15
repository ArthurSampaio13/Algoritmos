# O(n)
def busca_linear(array, valor):
    for i in range(len(array)):
        if valor == array[i]:
            return i
        else:
            return -1