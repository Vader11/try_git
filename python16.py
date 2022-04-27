value = input('input:')
value = [i for i in value.split(',') if int(i) % 2 != 0]
print(','.join(value))