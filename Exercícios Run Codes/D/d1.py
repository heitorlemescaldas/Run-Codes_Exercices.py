temperaturas  = []

temp = input('').split()


temperaturas = [int(t) for t in temp]

    
media = sum(temperaturas)/len(temperaturas)
soma_medias = 0
i = 0
while i < 7:
    if temperaturas[i] > media:
        soma_medias += 1
        i += 1
    else:
        i += 1
print(soma_medias)
       
