def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()

N, M = map(int, input("").split())
valores = list(map(int, input("").split()))
matriz = []

for i in range(N):
    linha = []
    for j in range(M):
        elemento = valores[i * M + j]
        linha.append(elemento)
    matriz.append(linha)


imprimir_matriz(matriz)






