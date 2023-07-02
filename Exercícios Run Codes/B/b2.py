l = float(input(''))
m = float(input(''))
a = float(input(''))
v = float(input(''))
multa = 0
if v > l:
    adicional = v - l
    multa = m + adicional * a
print(f'{multa:.2f}')
