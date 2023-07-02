n = int(input(""))
num1 = input().split()
num1 = [int(x1) for x1 in num1]
num2 = input().split()
num2 = [int(x2) for x2 in num2]
c = []
i = 0
while i < n:
    c.append(num1[i] + num2[i])
    i += 1
for c in c:
    print(c, end=' ')
print(" ", end=" ")
print(" ")

