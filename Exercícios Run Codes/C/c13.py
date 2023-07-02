n = int(input(''))
maior = None
menor = None
soma = 0
for i in range(n):
    num = int(input(''))
    soma += num
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
print(maior)
print(menor)
print(soma)
