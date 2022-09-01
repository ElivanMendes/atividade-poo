aux = 0
lower_value = ''
highest_value = ''

while aux < 5:
    number = int(input(f'Digite o {aux + 1} Valor: '))

    if aux == 0:
        lower_value = number
        highest_value = number
    else:
        if number < lower_value:
            lower_value = number
        elif number > highest_value:
            highest_value = number

    aux += 1

print(f'Menor Valor: {lower_value}\nMaior Valor: {highest_value}')
