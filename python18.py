import re

my_list = []
value = input('input:')
value = [x for x in value.split(',')]
for p in value:
    if (len(p) < 6) or (len(p) > 12):
        continue
    else:
        pass
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    else:
        pass
    my_list.append(p)
print(','.join(my_list))

