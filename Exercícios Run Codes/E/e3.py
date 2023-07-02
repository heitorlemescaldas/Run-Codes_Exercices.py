"""Faça um programa que leia uma string S e um caractere C. Ao fim escreva o número de vezes que o caractere C aparece na string S."""
string = input()
caractere = input()
i = 0
soma = 0
while i < len(string):
    if string[i] == caractere:
        soma += 1
    i += 1
print(soma)