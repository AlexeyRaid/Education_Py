# Завдання 3
# Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання, множення, ділення,
# зведення в ступінь, зведення до квадратного та кубічного коренів.
# Всі дані повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми.
# Кожна операція має бути реалізована у вигляді окремої функції.
# Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.
import re


def plus(a, b) -> float:
    return a + b


def minus(a, b) -> float:
    return a - b


def divide(a, b) -> float:
    if b == 0:
        return print("Ділення на нуль не можливе")

    else:
        return a / b


def multiply(a, b) -> float:
    return a * b


def degree(a, b) -> float:
    return a ** b


def square(a) -> float:
    return a ** 1 / 2


def cuberoot(a) -> float:
    return a ** 1 / 3


print('Введіть арифметичний вираз для (підтримується додавання, \n'
      'віднімання, ділення, множення, зведення в ступінь, зведення до квадратного та кубічного коренів \n'
      'Знаком додавання буде + \n'
      'Знаком віднімання буде -\n'
      'Знаком ділення буде /\n'
      'Знаком зведення двух чисел в ступінь буде ^\n'
      'Знаком зведення до квадратного кореня буде % \n'
      'Знаком зведення до кубічного кореня буде %%\n\n'
      'Для виходу з програми наберіть СТОП\n\n'
      'Приклад введення арифметичної дії\n'
      '2^4')
while True:
    choise = input().replace(',', '.')

    splitter = r"([+\-*\/^%]|%%)"
    math_list = list(re.split(splitter, choise))
    if choise.lower() == 'стоп':
        print('Дякую, що скористались нашим калькулятором')
        exit()

    try:
        a = float(math_list[0])
        b = float(math_list[2])
    except ValueError:
        print('Введіть будь ласка перше число, математичний знак, та друге математичне число\n'
              'Якщо ви хочете вийти з програми наберіть СТОП')
        continue
    else:
        a = float(math_list[0])
        b = float(math_list[2])
        m = math_list[1]
        match m:
            case '+':
                print(plus(a, b))
            case '-':
                print(minus(a, b))
            case '*':
                print(multiply(a, b))
            case '/':
                print(divide(a, b))
            case '^':
                print(degree(a, b))
            case '%':
                print(square(a))
            case '%%':
                print(cuberoot(a))

# Мені здалося цікавим розв'язати задачу, де калькулятор не буде питать 3 окремих значення у користувача - 1 значення, оператор та
# друге значення (якось неспортивно). Так значно красивіше.
# Недоліком є те, що приходиться вводить все одно 2 значення, навіть, якщо потрібно одне (корені)
# Також не зрозумів як побороти None при діленні на нуль (функція вертає None так як нічого не робить). Також було б непогано застосувати
# trim до значень словника math_list для тих, хто буде вводить через пробіли