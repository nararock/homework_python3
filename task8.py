my_string = input("Введите числа через пробел: ")
list_num = my_string.split()
numbers = []
for i in range(len(list_num)):
    numbers.append(int(list_num[i]))


def multiplication(my_list):
    len_list = len(my_list)
    new_list = []
    for j in range(len_list // 2):
        new_list.append(my_list[j] * my_list[len_list - 1 - j])
    if len_list % 2 != 0:
        new_list.append(pow(my_list[len_list // 2], 2))
    return new_list


print(multiplication(numbers))
