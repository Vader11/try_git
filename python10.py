values = input('input:')
values_list = values.split(' ')
values_set = set(values_list)
values_list = list(values_set)
values_list.sort()
values = ','.join(values_list)
print(values)