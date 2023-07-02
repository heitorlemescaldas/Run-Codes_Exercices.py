n = int(input(''))
lista = list(map(int, input().split()))
i = 0
par = []
impar = []
while i < n:
    if lista[i] % 2 == 0:
        par.append(lista[i])
    elif lista[i] % 2 != 0:
        impar.append(lista[i])
    i += 1
for par in par:
    print(par, end=' ')
print(" ", end=" ")
print(" ")
for impar in impar:
    print(impar, end=' ')
print(" ", end=" ")
print(" ")
