my_values = input('input:')
my_dict = {'digit': 0, 'letters': 0}
for i in my_values:
    if i.isdigit():
        my_dict['digit'] += 1
    if i.isalpha():
        my_dict['letters'] += 1
print(f"digit:{my_dict['digit']},letters:{my_dict['letters']}")
