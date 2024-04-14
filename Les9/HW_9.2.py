# Завдання 2
# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.
import re

phrase = input('Введіть текст: \n').lower()
phrase = re.sub(r'[^a-zA-Zа-яА-Я]', '', phrase)

clear_phrase = phrase[::-1]

if clear_phrase == phrase:
    print('Ваша фраза є паліндромом')
else:
    print('Ваша фраза не паліндром')
