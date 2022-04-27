line = []
while True:
    my_str = input('input:')
    if my_str:
        line.append(my_str.upper())
    else:
        break
for i in line:
    print(i)
