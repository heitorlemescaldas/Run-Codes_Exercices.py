num = int(input(''))
par = 0
impar = 0
somapar = 0
somaimpar = 0
soma = 0
while num > 0:
    if num % 2 == 0:
        par += 1
        somapar += num
    else:
        impar += 1
        somaimpar += num
    soma += num
    num = int(input(''))
print(somapar)
print(somaimpar)
print(soma)
    
