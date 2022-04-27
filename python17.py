amount = 0
while True:
    value = input('input:')
    if not value:
        break
    value = value.split(' ')
    if value[0] == 'D':
        amount += int(value[1])
    elif value[0] == 'W':
        amount -= int(value[1])
    else:
        pass
print(f'amount:{amount}')
