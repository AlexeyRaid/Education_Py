# Завдання 4
# Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.

def sum_nat(a, b):
    if a > b:
        return 0
    return a + sum_nat(a + 1, b)


a = int(input("Введіть перше наруральне число для проміжку "))
b = int(input("Введіть друге наруральне число для проміжку "))

print('Сума наруральних чисел в заданому вами проміжку дорівнює ', sum_nat(a, b))
