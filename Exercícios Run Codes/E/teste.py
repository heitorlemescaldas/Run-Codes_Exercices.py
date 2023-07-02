def sao_anagramas(string1, string2):
    # Remover espaços das strings
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    
    # Verificar se as strings têm o mesmo comprimento
    if len(string1) != len(string2):
        return False
    
    # Converter as strings em listas para facilitar a manipulação
    lista1 = list(string1)
    lista2 = list(string2)
    
    # Ordenar as listas em ordem alfabética
    lista1.sort()
    lista2.sort()
    
    # Verificar se as listas são iguais (anagramas)
    return lista1 == lista2

# Ler as duas strings do usuário
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Verificar se são anagramas e imprimir o resultado
if sao_anagramas(string1, string2):
    print("1")
else:
    print("0")