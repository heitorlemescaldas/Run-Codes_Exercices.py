a = int(input(''))
b = int(input(''))
c = int(input(''))
if a + b < c or a + c < b or b + c < a:
    print('INVALIDO')
elif a != b and a != c and b != c:
    print('ESCALENO')
elif a == b and a == c and b == c:
    print('EQUILATERO')
else:
    print('ISOSCELES')
