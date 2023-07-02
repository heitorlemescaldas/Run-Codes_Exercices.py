num = int(input(''))
if num == 0 or num == 1:
    print('1')
else:
    for i in range(num-1,1,-1):
        num *= i
    print(num)
    
