n = int(input(''))
soma = 0
while n > 0:
    resto = n % 10
    soma += resto
    n //= 10
print(soma)
