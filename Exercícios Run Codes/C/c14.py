n = int(input(''))
c = int(input(''))
m = int(input(''))
consegue_comprar = n/c
embalagens = consegue_comprar
while embalagens >= m:
    num_trocas = embalagens // m
    consegue_comprar += num_trocas
    embalagens = num_trocas + embalagens % m
if consegue_comprar <= 0:
    print(0)
print(f'{consegue_comprar:.0f}')
    
