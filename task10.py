def to_binary(number):
    result = []
    while number // 2 > 1:
        result.append(number % 2)
        number //= 2
    result.append(number % 2)
    result.append(number // 2)
    result.reverse()
    return result


num = int(input('Введите число: '))
print(to_binary(num))
