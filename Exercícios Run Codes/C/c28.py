n = int(input(''))
conjunto = []
i = 0
while i < n:
    numero = int(input(''.format(i+1)))
    conjunto.append(numero)
    i += 1

tamanho_maximo = 1
tamanho_atual = 1
for i in range(1, n):
    if conjunto[i] >= conjunto[i-1]:
        tamanho_atual += 1
    else:
        if tamanho_atual > tamanho_maximo:
            tamanho_maximo = tamanho_atual
        tamanho_atual = 1

if tamanho_atual > tamanho_maximo:
    tamanho_maximo = tamanho_atual

print(tamanho_maximo)
