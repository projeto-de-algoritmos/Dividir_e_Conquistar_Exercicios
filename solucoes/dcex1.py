def maxima_soma_ponto_medio(numeros, esquerda, medio, direita):
    soma_esquerda = float('-inf')
    soma_atual = 0

    for i in range(medio, esquerda - 1, -1):
        soma_atual += numeros[i]
        soma_esquerda = max(soma_esquerda, soma_atual)

    soma_direita = float('-inf')
    soma_atual = 0

    for i in range(medio + 1, direita + 1):
        soma_atual += numeros[i]
        soma_direita = max(soma_direita, soma_atual)

    return soma_esquerda + soma_direita

def maximo_subarray_soma_dc(numeros, esquerda, direita):
    if esquerda == direita:
        return numeros[esquerda]

    medio = (esquerda + direita) // 2

    return max(
        maximo_subarray_soma_dc(numeros, esquerda, medio),
        maximo_subarray_soma_dc(numeros, medio + 1, direita),
        maxima_soma_ponto_medio(numeros, esquerda, medio, direita)
    )

# Exemplos:
numeros1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado1 = maximo_subarray_soma_dc(numeros1, 0, len(numeros1) - 1)
print(resultado1)  # 6 [4,-1,2,1]

numeros2 = [1]
resultado2 = maximo_subarray_soma_dc(numeros2, 0, len(numeros2) - 1)
print(resultado2)  # 1 [1]

numeros3 = [5, 4, -1, 7, 8]
resultado3 = maximo_subarray_soma_dc(numeros3, 0, len(numeros3) - 1)
print(resultado3)  # 23 [5,4,-1,7,8]
