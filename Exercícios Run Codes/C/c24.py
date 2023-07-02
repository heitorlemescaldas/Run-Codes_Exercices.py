N = int(input(''))
lista = []
maiores = []
i = 0
while i < N:
    num = int(input(''))
    lista.append(num)
    i += 1
lista.sort(reverse=True)
maior1 = lista[0]
maior2 = lista[1]
print(maior1)
print(maior2)

