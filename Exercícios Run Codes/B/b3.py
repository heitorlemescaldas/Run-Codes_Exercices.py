idade =  int(input(''))
if idade == 16 or idade == 17:
    print('FACULTATIVO')
elif idade >= 18 and idade <= 69:
    print('OBRIGATORIO')
else:
    print('DISPENSADO')
