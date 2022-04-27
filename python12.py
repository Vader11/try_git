my_list = []
for i in range(1000, 2001):
    if i % 2 == 0:
        my_list.append(str(i))
print(','.join(my_list))
