import math

c = 50
h = 30

values = input('input num:')
values = values.split(',')
values = [float(i) for i in values]

output = [int(math.sqrt(2 * c * i / h)) for i in values]
print(output)
