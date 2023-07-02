idades = []
idade = int(input(''))
while idade >= 0:
    idades.append(idade)
    idade = int(input(''))
media = sum(idades)/len(idades)
maior_18 = 0
idosos = 0
i = 0
while i < len(idades):
    if idades[i] >= 18:
        maior_18 += 1
    if idades[i] > 75:
        idosos += 1
    i += 1
media_idosos = (idosos/len(idades)) * 100

print(f'{media:.2f}')
print(f'{maior_18:.0f}')
print(f'{media_idosos:.2f}%')

        
        
    
