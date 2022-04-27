from operator import itemgetter

l = []
while True:
    value = input('input:')
    if not value:
        break
    l.append(tuple(value.split(',')))
l = sorted(l, key=itemgetter(0, 1, 2))
print(l)
