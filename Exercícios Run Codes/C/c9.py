n = int(input(''))
a = 1
b = 1
for i in range(n):
    print(f'{a}', end=' ')
    a, b = b, a + b
    
    

