num = int(input(""))
unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = num // 1000
num_invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar

print(f"{num_invertido}")
