def my_func(x, y):
    # 1-ый способ решения
    result1 = 1
    for el in range(abs(y)):
        result1 *= x
    # 2-ой способ решения
    temp = 0
    result2 = x
    if y == 0:
        result2 = 1
    else:
        for el in range(abs(y) - 1):
            for num in range(int(x)):
                temp += result2
            result2 = temp + result2 * (x - round(x, 0))
            temp = 0
    return 1 / result1, 1 / result2


num_1 = float(input("Введите основание: "))
num_2 = int(input("Введите отрицательную степень числа: "))
res1, res2 = my_func(num_1, num_2)
print(f'{res1}, {res2}')
