s = float(input(''))
dias = s // 86400
s = s % 86400

horas = s // 3600
s = s % 3600

minutos = s // 60
segundos = s % 60

print(f'{dias:.0f} {horas:.0f} {minutos:.0f} {segundos:.0f}')
