def anagrama(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    if len(str1) != len(str2):
        return False
    lista1 = list(str1)
    lista2 = list(str2)
    lista1.sort()
    lista2.sort()
    return lista1 == lista2


string_1 = input()
string_2 = input()
if anagrama(string_1, string_2):
    print(1)
else:
    print(0)
