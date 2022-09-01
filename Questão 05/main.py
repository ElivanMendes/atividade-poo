aux = 0
sum = 0

while aux < 10:
    number = input(f'Digite o {aux + 1} Valor Interiro: ')
    sum += int(number)
    aux += 1

print('Media dos Valores:', sum / 10)
