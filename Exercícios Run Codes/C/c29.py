num = int(input(''))
reverso = 0
original = num
while num > 0:
    reverso = reverso * 10 + num % 10
    num //= 10
if reverso == original:
    print('S')
else:
    print('N')
    
