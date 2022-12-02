def get_fibonacci(number):
    fibonacci1 = [0, 1]
    fibonacci2 = [0, 1]
    for i in range(2, number + 1):
        fibonacci1.append(fibonacci1[i - 1] + fibonacci1[i - 2])
        fibonacci2.append(fibonacci2[i - 2] - fibonacci2[i - 1])
    fibonacci2.reverse()
    fibonacci2.pop()
    fibonacci = fibonacci2 + fibonacci1
    return fibonacci


num = int(input('Введите число: '))
print(get_fibonacci(num))
