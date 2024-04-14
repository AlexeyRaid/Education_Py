def quadratic_equation(a, b, c):
    x1, x2 = None, None

    def calc_rezult(a, b, c):
        nonlocal x1, x2
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
        elif discriminant == 0:
            x1 = x2 = -b / (2 * a)

    calc_rezult(a, b, c)
    return x1, x2


a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
c = float(input("Введіть значення c: "))

rezult = quadratic_equation(a, b, c)
print("Корені квадратного рівняння:", rezult)
