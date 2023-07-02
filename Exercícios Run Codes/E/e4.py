def palindromo(string):
    string = string.replace(" ", "")
    return string == string[::-1]

string = input()

if palindromo(string):
    print(1)
else:
    print(0)