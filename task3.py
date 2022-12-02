def get_sum(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    max_1 = max(my_list)
    my_list.remove(max_1)
    max_2 = max(my_list)
    return max_1 + max_2


print(f'сумма наибольших двух из (1, 2, 3) равна {get_sum(1, 2, 3)}')
print(f'сумма наибольших двух из (3, 3, 3) равна {get_sum(3, 3, 3)}')
print(f'сумма наибольших двух из (4, 3, 4) равна {get_sum(4, 3, 4)}')
