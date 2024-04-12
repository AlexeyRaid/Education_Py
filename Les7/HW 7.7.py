# Завдання 7
# Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до структури(реалізуйте інтерфейс(меню),
# за допомогою якого можна робити маніпуляції з даними):
# прізвище:
#     посада: ...
#     досвід роботи: …
#     портфоліо: …
#     коефіцієнт ефективності: …
#     стек технологій: …
#     зарплата: …
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.

# Розблокувати для роботи бойової
# employeers = {}

# Розблокувати для тестів
employeers = {
    "Іванов Іван": ["Менеджер", 5, "Управління проектами", 4.5, "Python, SQL", 5000],
    "Петров Петро": ["Розробник програмного забезпечення", 3, "Веб-розробка", 4.0, "JavaScript, HTML, CSS", 4500],
    "Марія Маринина": ["Data Scientist", 2, "Машинне навчання", 4.2, "Python, R, TensorFlow", 5500],
    "Оксана Олександрівна": ["Системний адміністратор", 4, "IT-інфраструктура", 4.3, "Linux, Windows Server", 4800]
}

while True:
    choise = input('\n'
                   '\t \t Меню\n'
                   '1 - Ввести нові дані\n'
                   '2 - Переглянути дані працівників \n'
                   '3 - Змінити дані працівника \n'
                   '4 - Рейтинг працівників\n'
                   '5 - Вихід з програми\n'
                   '\n'
                   'Зробіть ваш вибір\n'
                   '\t\t\t')

    match choise:
        case '1':
            print(
                'Послідовно введіть ПІБ працівника, посаду, досвід роботи, портфоліо, коефіцієнт ефективності, стек технологій та зарплату\n'
                'Для закінчення введення залиште будь який рядок порожнім (просто натисніть Ентер\n')
            while True:
                emp_fio = input('\nВведіть ПІБ працівника ')
                if emp_fio == '':
                    print('Вихід в основне меню')
                    break

                emp_post = input(f'\n Введіть посаду для {emp_fio} ')
                if emp_post == '':
                    print('Вихід в основне меню')
                    break

                emp_exp = int(input(f'\n Введіть стаж роботи для {emp_fio} (повних місяців) '))
                if emp_exp == '':
                    print('Вихід в основне меню')
                    break

                emp_pfolio = input(f'\n Розпишіть портфоліо для працівника {emp_fio} ')
                if emp_pfolio == '':
                    print('Вихід в основне меню')
                    break

                emp_coeff = float(input(f'\n Введіть коефіцієнт {emp_fio} в баллах '))
                if emp_coeff == '':
                    print('Вихід в основне меню')
                    break

                emp_tech = input(f'\n Розпишіть стек технологій {emp_fio} ')
                if emp_tech == '':
                    break

                emp_salary = float(input(f'\n Введіть зарплату співробітника {emp_fio} '))
                if emp_salary == '':
                    break
                employeers[emp_fio] = [emp_post, emp_exp, emp_pfolio, emp_coeff, emp_tech, emp_salary]
                print(f'Дякую, новий співробітник доданий. Його дані: \n {emp_fio}')
                emp_list = employeers[emp_fio]
                print(
                    f' Посада: {emp_list[0]} \n Стаж роботи: {emp_list[1]} \n Портфоліо: {emp_list[2]} \n Коефіцієнт ефективності: {emp_list[3]} \n Стек технологій: {emp_list[4]} \n Зарплата: {emp_list[5]}')

        case '2':
            print('Список співробітників (по алфавіту) \n')
            fio_list = employeers.keys()
            srtd_fio = sorted(fio_list)
            for fio in srtd_fio:
                print(fio)

        case '3':
            ch_emp = input('Введіть ПІБ працівника для редагування ')
            if ch_emp not in employeers:
                print('Ой, я не знайшов такого співробітника.... ')
            else:
                old_emp = employeers[ch_emp]
                ch3 = int(input('Які дані потрібно замінити? \n'
                                '1- ПІБ \n'
                                '2- Посаду \n'
                                '3- Досвід роботи \n'
                                '4- Портфоліо \n'
                                '5- Коефіцієнт ефективності \n'
                                '6- Стек технологій \n'
                                '7- Зарплату \n'
                                '8- Вихід \n'))
                new_data = input('Введіть оновлені дані \n')
                if ch3 == 1:
                    employeers.pop(ch_emp)
                    employeers.update({new_data: old_emp})
                    print('Дані замінено на: \n')
                    print(f'Прізвище {new_data}')
                    emp_list = employeers.get(new_data)
                    print(
                        f' Посада: {emp_list[0]} \n Стаж роботи: {emp_list[1]} \n Портфоліо: {emp_list[2]} \n Коефіцієнт ефективності: {emp_list[3]} \n Стек технологій: {emp_list[4]} \n Зарплата: {emp_list[5]}')
                elif ch3 in (2, 3, 4, 5, 6, 7):
                    employeers[ch_emp][ch3 - 1] = new_data
                    print('Дані замінено на: \n')
                    print(f'Прізвище {ch_emp}')
                    emp_list = employeers[ch_emp]
                    print(
                        f' Посада: {emp_list[0]} \n Стаж роботи: {emp_list[1]} \n Портфоліо: {emp_list[2]} \n Коефіцієнт ефективності: {emp_list[3]} \n Стек технологій: {emp_list[4]} \n Зарплата: {emp_list[5]}')
        case '4':
            print('Рейтинг працівників: \n')
            rating_dict = {}
            for key, value in employeers.items():
                rating_dict[key] = value[3]
            sorted_rating = dict(sorted(rating_dict.items(), key=lambda item: item[1], reverse=True))
            for key, value in sorted_rating.items():
                print(f'{key}: {value}')

        case '5':
            exit()
