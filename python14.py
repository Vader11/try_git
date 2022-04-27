values = input('inputs:')
my_dict = {'upcase': 0, 'lowcase': 0}
for i in values:
    if i.isupper():
        my_dict['upcase'] += 1
    if i.islower():
        my_dict['lowcase'] += 1
print(f"upcase:{my_dict['upcase']},lowcase:{my_dict['lowcase']}")

