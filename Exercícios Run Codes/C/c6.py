n = int(input(''))
num = 1
den = 1
s = 0
while den <= n:
    s = s + (num/den)
    den += 1
print(f'{s:.4f}')
