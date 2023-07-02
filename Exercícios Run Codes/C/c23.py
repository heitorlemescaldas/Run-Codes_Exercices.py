idade = int(input(''))
tam_velas = []
maioresvelas = []
maxvelas = 0
i = 0
while i < idade:
    velas = int(input(''))
    tam_velas.append(velas)
    i += 1

i = 0
while i < len(tam_velas):
    if tam_velas[i] == max(tam_velas):
        maxvelas += 1
    i += 1
print(maxvelas)
    
    

        
