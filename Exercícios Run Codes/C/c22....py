p1 = int(input(''))
pulo1 = int(input(''))
p2 = int(input(''))
pulo2 = int(input(''))
if (p2 > p1 and pulo1 > pulo2 and (p2 - p1) % (pulo2 - pulo1) == 0) or (p1 > p2 and pulo2 > pulo1 and (p1 - p2) % (pulo1 - pulo2) == 0):
    print('SIM')
elif p1 == p2:
    print('SIM')
else:
    print('NAO')
