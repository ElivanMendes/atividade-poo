aux = 0
sum = 0

while aux < 10:
    number = input(f'Digite o {aux + 1} Valor: ')
    sum += int(number)
    aux += 1

print('Soma Total dos Valores:', sum)
