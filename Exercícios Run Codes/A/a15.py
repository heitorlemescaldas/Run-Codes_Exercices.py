eleitores = int(input(""))
brancos = int(input(""))
nulos = int(input(""))
validos = int(input(""))

total_votos = brancos + nulos + validos
porcentagem_brancos = (brancos / eleitores) * 100
porcentagem_nulos = (nulos / eleitores) * 100
porcentagem_validos = (validos / eleitores) * 100
porcentagem_ausentes = ((eleitores - total_votos) / eleitores) * 100

print(f"Nulos: {porcentagem_nulos:.2f}%")
print(f"Brancos: {porcentagem_brancos:.2f}%")
print(f"Validos: {porcentagem_validos:.2f}%")
print(f"Ausentes: {porcentagem_ausentes:.2f}%")
