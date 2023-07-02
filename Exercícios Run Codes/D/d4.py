n = int(input(''))
lista = list(map(int, input().split()))
x = int(input(''))
i = 0
lista_falsa = []
while i < len(lista):
    if lista[i] == x and i < len(lista):
        print(i)
        break
    elif lista[i] != x:
        lista_falsa.append(lista[i])
    i += 1
if len(lista_falsa) == len(lista):
    print('-1')


