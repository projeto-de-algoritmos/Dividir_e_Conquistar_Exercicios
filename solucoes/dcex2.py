class TreeNode:
    def __init__(self, val=0, esquerda=None, direita=None):
        self.val = val
        self.esquerda = esquerda
        self.direita = direita

def construirArvoreBinariaMaxima(numeros):
    if not numeros:
        return None
    
    max_index = numeros.index(max(numeros))
    
    raiz = TreeNode(numeros[max_index])
    
    raiz.esquerda = construirArvoreBinariaMaxima(numeros[:max_index])
    raiz.direita = construirArvoreBinariaMaxima(numeros[max_index + 1:])
    
    return raiz

# Exemplos:
numeros1 = [3, 2, 1, 6, 0, 5]
arvore1 = construirArvoreBinariaMaxima(numeros1)
# [6,3,5,null,2,0,null,null,1]

numeros2 = [3, 2, 1]
arvore2 = construirArvoreBinariaMaxima(numeros2)
# [3,null,2,null,1]
