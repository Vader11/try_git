import re

value = input('please input :')
my_list = value.split(',')
print(my_list)

my_list = re.findall(r'[0-9]+', value)
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)
