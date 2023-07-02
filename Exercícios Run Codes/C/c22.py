x1 = int(input(''))
x2 = int(input(''))
v1 = int(input(''))
v2 = int(input(''))
i = 1
if x1+v1 > x2+v2:
    while i < x1+v1:
        x1+(v2*i) == x2+(v2*i)
        print('SIM')
        break
i = 1
if x1+v1 < x2+v2:
    while i < x2+v2:
        x1+(v1*i) == x2+(v2*i)
        print('SIM')
        break
else:
    print('NAO')
    
