def get_sum():
    my_sum = 0
    flag = False
    while True:
        if flag:
            break
        numbers = input('Введите числа: ')
        list_num = numbers.split()
        for el in list_num:
            if el.isnumeric():
                my_sum += int(el)
            else:
                flag = True
                break
        print(f'Сумма: {my_sum}')


get_sum()
