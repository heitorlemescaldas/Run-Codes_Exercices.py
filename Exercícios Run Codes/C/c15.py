num = int(input(''))
if num <= 1:
    print(0)
else:
    for i in range (2, num):
        if num % i == 0:
            print(0)
            break
    else:
        print(1)
    
            
