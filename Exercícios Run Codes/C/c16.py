def eh_primo(num):
    """Verifica se um número é primo"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input(""))
soma = 0

for i in range(1, n+1):
    if eh_primo(i):
        soma += i

print(soma)
    
