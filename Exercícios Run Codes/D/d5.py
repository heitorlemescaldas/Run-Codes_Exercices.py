n = int(input(''))
lista = []
lista = list(map(int, input().split()))
x = int(input(''))
iguais = 0
i = 0
while i < n:
    if x == lista[i]:
        iguais += 1
    i += 1
print(iguais)
        
