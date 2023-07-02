# Função para imprimir a matriz em formato matricial
def imprimir_matriz_com_soma(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()

# Lendo as dimensões da matriz
N, M = map(int, input("").split())

# Lendo os valores da matriz em uma única linha
valores = list(map(int, input("").split()))

# Criando a matriz com os valores lidos
matriz = []
for i in range(N):
    linha = []
    soma = 0
    for j in range(M):
        elemento = valores[i * M + j]
        soma += elemento
    linha.append(soma)
    matriz.append(linha)

# Imprimindo a matriz em formato matricial
imprimir_matriz_com_soma(matriz)