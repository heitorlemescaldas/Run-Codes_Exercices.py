def  ler_matriz():
    # Lê as dimensões da matriz
    n, m = map(int, input("").split())

    matriz = []

    # Lê os valores da matriz em uma única linha
    valores = input("").split()

    # Converte os valores para inteiros e adiciona à matriz
    for i in range(n):
        linha = []
        for j in range(m):
            valor = int(valores[i * m + j])
            linha.append(valor)
        matriz.append(linha)

    return matriz


def imprimir_soma_colunas(matriz):
    num_colunas = len(matriz[0])
    soma_colunas = [0] * num_colunas

    # Calcula a soma de cada coluna
    for linha in matriz:
        for j in range(num_colunas):
            soma_colunas[j] += linha[j]

    # Imprime a soma de cada coluna
    for soma in soma_colunas:
        print(soma)



# Chama as funções para ler a matriz e imprimir a soma das colunas
matriz = ler_matriz()
imprimir_soma_colunas(matriz)