n = int(input(""))

# inicializa a soma dos fatoriais e o contador
soma = 0
i = 0

# loop para calcular o fatorial de cada número de 0 até N
while i <= n:
    # calcula o fatorial de i
    fatorial = 1
    j = 1
    while j <= i:
        fatorial *= j
        j += 1
    # adiciona o fatorial à soma
    soma += fatorial
    i += 1

# imprime a soma dos fatoriais
print(soma)
