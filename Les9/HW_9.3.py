# Завдання 3
# Нехай на кожну сходинку можна стати з попередньої або переступивши через одну.
# Визначте, скількома способами можна піднятися на задану сходинку.

n = int(input('Введіть кількість сходинок: '))

if n == 1 or n == 2:
    print(f'Кількість варіантів - {n}')
else:
    rr = [0] * (n + 1)
    rr[1] = 1
    rr[2] = 2
    for i in range(3, n + 1):
        rr[i] = rr[i - 1] + rr[i - 2]
    print(f'Кількість варіантів - {rr[n]}')
