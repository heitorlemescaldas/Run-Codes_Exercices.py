n = int(input(""))
valores = input("").split()
valores = [int(valor) for valor in valores]
for i in range(0, n-1, 2):
    valores[i], valores[i+1] = valores[i+1], valores[i]
for valores in valores:
    print(valores, end=' ')
print(" ", end=" ")
print(" ")
                         

    

