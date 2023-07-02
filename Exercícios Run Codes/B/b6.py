import math
a = float(input(''))
b = float(input(''))
c = float(input(''))
delta = b**2 - 4*a*c
x1 = (-1*b + delta**(1/2))/(2*a)
x2 = (-1*b - delta**(1/2))/(2*a)
soma = x1 + x2
if delta < 0:
    print(math.nan)
else:
    print(f'{soma:.2f}')

#da pra fazer sem a biblioteca tbm(import.math), apenas trocar o print(math.nan) para print('nan')
