number_1 = float(input("Введите делимое: "))
number_2 = float(input("Введите делитель: "))


def divide(var_1, var_2):
    try:
        answer = var_1 / var_2
    except ZeroDivisionError:
        return "Вы делите на ноль!"
    else:
        return round(answer, 2)


print(f'Частное: {divide(number_1, number_2)}')
