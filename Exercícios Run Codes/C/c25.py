N = int(input(''))
lista = []
i = 0
while i < N:
    num = int(input(''))
    lista.append(num)
    i += 1
if max(lista) == lista[N-1] and min(lista) == lista[0]:
    print('1')
elif max(lista) == lista[0] and min(lista) == lista[N-1]:
    print('-1')
else:
    print('0')
