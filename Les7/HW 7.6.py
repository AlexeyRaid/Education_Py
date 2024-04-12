# Завдання 6
# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою: автор: твір. Передбачте можливість виведення на екран сортування за автором та твором.

dct = {
    'Леся Українка': 'Лісова пісня',
    'Тарас Шевченко': 'Кобзар',
    'Іван Франко': 'Захар Беркут',
    'Михайло Коцюбинський': 'Тіні забутих предків',
    'Ліна Костенко': 'Маруся Чурай',
    'Остап Вишня': 'Буря',
    'Павло Загребельний': 'Два кольори',
    'Василь Стефаник': 'Камінний хрест',
    'Марко Вовчок': 'Місяць',
    'Іван Нечуй-Левицький': 'Кайдашева сім’я',
    'Ольга Кобилянська': 'Земля',
    'Василь Короленко': 'Сліпий музикант',
    'Микола Гоголь': 'Мертві душі',
    'Іван Багряний': 'Тигролови',
    'Максим Рильський': 'Енеїда',
    'Михайло Старицький': 'Слово о полку Ігоревім',
    'Олександр Довженко': 'Зачарована Десна',
    'Марія Матіос': 'Синів пісні',
    'Володимир Винниченко': 'Життя',
    'Олесь Гончар': 'Собор',
    'Іван Котляревський': 'Енеїда',
    'Марко Цебрій': 'Чорна рада',
    'Василь Шкляр': 'Берегиня'
}

q = input(
    'Якщо ви хочете змінити значення Автора введіть 1, якщо Твору - введіть 2, якщо бажаєте перейти до сортування - введіть будь-яке інше значення ')
if q == '2':
    find_word = input('Введіть назву твору, який ви хочете змінити ')
    for key_aut, val_word in dct.items():
        if find_word == val_word:
            new_word = input('Введіть змінену назву твору ')
            dct[key_aut] = new_word
            break
        else:
            continue
    print('Такого твору не знайдено')
elif q == '1':
    find_aut = input('Введіть назву автора, якого ви хочете змінити ')
    if find_aut in dct:
        new_aut = input('Введіть змінену назву Автора ')
        old_word = dct.get(find_aut)
        dct.pop(find_aut)
        dct[new_aut] = old_word
    else:
        print('Такого автора не знайдено')

# Варіанти сортування

srtd = input('Ведіть 1, якщо бажаєте відсортувати по автору, або 2, якщо бажаєте відсортувати по твору ')

if srtd == '1':
    sorted_aut = sorted(dct)
    print(' ')
    print('Сортування по автору:')
    for aut in sorted_aut:
        print(aut, ' ', dct.get(aut))
elif srtd == '2':
    sorted_work = sorted(dct.values())
    print('Сортування по твору')
    for wrk in sorted_work:
        for key, value in dct.items():
            if wrk == value:
                print(key, ' ', wrk)
else:
    print('Дякую, що ви з нами. Допобачення')

# Звичайно, при зміні Твору потрібно перевіряти, чи не декільком авторам належить такий твір (напр. Енеїда),
# і якщо так - ще запропонувати вибрати автора, твір якого маємо замінити. Але це вже не на домашнє завдання тягне, а на курсову...
# Також слабе місце цієї програми, використані словники, а ключ словника (Автор) має бути унікальним, що унеможливлює дублювання.
# Можливо з цього є вихід (але в межах того, що ми вивчили я поки не бачу як це зробить)