n = int(input(""))
i = 1
# Verifica se n é produto de três números inteiros consecutivos
while i < n:
    if i*(i+1)*(i+2) == n:
        print("S")
        break
    i += 1
else:
    print("N")
