def int_func(word):
    return word.capitalize()


my_string = input("Введите строку: ")
for el in my_string.split():
    print(int_func(el), end=' ')
