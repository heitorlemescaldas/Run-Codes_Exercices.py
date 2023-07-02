a = int(input(''))
b = int(input(''))
res = 1
for i in range(b):
    temp = 0
    for j in range(a):
        temp += res
    res = temp
print(res)
    

