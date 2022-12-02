my_string = input("Введите числа через пробел: ")
list_num = my_string.split()
numbers = []
for i in range(len(list_num)):
    numbers.append(int(list_num[i]))


def get_sum(my_list):
    my_sum = 0
    for j in range(1, len(my_list), 2):
        my_sum += my_list[j]
    return my_sum


print(f'Сумма элементов, стоящих на нечётной позиции: {get_sum(numbers)}')
