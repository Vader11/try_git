x_y_list = input('input_num:')
x_y_list = [int(i) for i in x_y_list.split(',')]
x = x_y_list[0]
y = x_y_list[1]

mult_list = [[0 for j in range(x)] for i in range(y)]
# print(mult_list)

for i in range(y):
    for j in range(x):
        mult_list[i][j] = i * j
print(mult_list)
