N = int(input(''))
lista = []
posicao = 0
lista = list(map(int, input().split()))
i = 0
maior = lista[i]
while i < N:
    if lista[i] > maior:
        maior = lista[i]
        posicao = i
    i += 1
print(maior)
print(posicao)

