my_value = input('input:')
my_value = my_value.split(',')

my_list = []
for i_b in my_value:
    i = int(i_b, 2)
    if i % 5 == 0:
        my_list.append(i_b)
print(','.join(my_list))
