# O(Log2 N)
def busca_binaria(array, valor):
    limite_inferior = 0
    limite_superior = len(array) - 1
    
    while limite_inferior <= limite_superior:
        meio = int((limite_superior + limite_inferior) / 2)
        chute = array[meio]
        
        if chute == valor:
            return meio
        
        elif chute < valor:
            limite_inferior = meio + 1
        
        else: 
            limite_superior = meio - 1
        
    return -1
            