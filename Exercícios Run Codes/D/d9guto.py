n = int(input())
count = 0
soma = 0
L = list(map(int, input().split()))
A = list(map(int, input().split()))
if A[0] <= A[1]:
    i = A[0]
    j = A[1]
else:
    i = A[1]
    j = A[0]
if i > (n-1) or j > (n-1):
    print('INVALIDO')
else:
    while i <= j:
        soma += L[i]
        i += 1
    print(soma)
