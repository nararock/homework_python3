my_string = input("Введите вещественные числа через пробел: ")
list_num = my_string.split()
numbers = []
for i in range(len(list_num)):
    numbers.append(float(list_num[i]))


def find_diff(my_list):
    max_diff = 0
    for k in range(len(my_list)):
        for j in range(k, len(my_list)):
            if abs((my_list[k] - int(my_list[k]))
                   - (my_list[j] - int(my_list[j]))) > max_diff:
                max_diff = abs((my_list[k] - int(my_list[k]))
                               - (my_list[j] - int(my_list[j])))
    return max_diff


print(find_diff(numbers))
