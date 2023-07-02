n = int(input(''))
divisores = 0
for i in range(1, n): #n consegui fazer com while
    if n % i == 0:
        divisores += i
if divisores == n:
    print('S')
else:
    print('N')
    

        
