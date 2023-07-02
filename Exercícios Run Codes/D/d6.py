n = int(input(""))
valores = input("").split()


valores = [int(valor) for valor in valores]


for valor in reversed(valores):
    print(valor, end=" ")
