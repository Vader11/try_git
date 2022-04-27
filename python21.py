import math

location = [0, 0]
while True:
    value = input('input:')
    if not value:
        break
    value = value.split(' ')
    direction = value[0]
    step = int(value[1])
    if direction == 'UP':
        location[1] += step
    if direction == 'DOWN':
        location[1] -= step
    if direction == 'LETF':
        location[0] -= step
    if direction == 'RIGHT':
        location[0] += step
distance = math.sqrt(location[0] ** 2 + location[1] ** 2)
print(distance)
