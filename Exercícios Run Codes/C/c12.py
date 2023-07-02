n = int(input(''))
maior = None
for i in range(n):
    num = int(input(''))
    if maior is None or num > maior:
        maior = num
print(maior)
    

    
