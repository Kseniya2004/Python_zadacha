import time

import pandas

csv_file = None
# Сброс ограничений на число столбцов
pandas.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pandas.set_option('display.max_colwidth', None)
menu = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'По пункту назначения',
    '5': 'По интервалу времени',
    '6': 'Станции поезда',
    '7': 'Количество поездов, идущих из станции',
    '8': 'Среднее время в пути',
    '9': 'Сохранить в файл',
    '0': '<-Меню',
    'exit': 'Выход'
}


# 1. Функция открытия файла
def file_open():
    try:
        data = pandas.read_csv('data.csv', delimiter=";")
    except Exception as e:
        print(e)
    print('Файл открыт. Записей: ', len(data.index))
    return data


# 2. Функция добавления
def insert(des, dep_point, num, dep_time, trav_time, stat):
    global csv_file
    df_insert = pandas.DataFrame([(max(csv_file['№'] + 1), des, dep_point, num, dep_time, trav_time, stat)],
                                 columns=('№', 'Пункт_назнач.', 'Пункт_отправ.', 'Номер_поезда', 'Вр._Отправления',
                                          'Вр._в_пути(мин.)', 'Станции'))
    df2 = pandas.concat([csv_file, df_insert])
    return df2


# 3. Функция удаления
def drop_by_arg(val, col_name='Номер поезда'):
    global csv_file
    if col_name == '№':
        val = int(val)
    csv_file = csv_file.set_index(col_name)
    csv_file.drop(val, axis=0, inplace=True)
    print(csv_file)


# 4. Поиск по пункту назначения
def find_des(val, col_name='Пункт назнач.'):
    df = csv_file[csv_file[col_name].isin([val])]
    print(df)


# 5. Поиск интервалу времени
def find_time(val, col_name='Вр. Отправления'):
    pass


# 6. Станции поезда
def station_train(val, col_name='Номер поезда'):
    global csv_file
    if col_name == '№':
        val = int(val)
    df = csv_file[csv_file['Номер поезда'].isin(val['Номер поезда'])]
    print(df)

# 7. Количесвто поездов идущих из станции


# 8. Среднее время пути всех поездов
def avg_time():
    print("Среднее время в пути:", csv_file["Вр. в пути(мин.)"].mean())


# 9. Сохранение
def save():
    try:
        csv_file.to_csv('data.csv', index=False, sep=';')
    except Exception as e:
        print(e)


# Вывод меню
print('\n'.join([f"{k} : {v}" for k, v in menu.items()]))
while True:
    comand = input()
    if comand == '1':
        csv_file = file_open()
    elif comand == '2':
        csv_file = insert(input('Пункт назначения: '), input('Пункт отправления: '),
                          int(input('Номер поезда: ')), (input('Время отправления: ')),
                          int(input('Время в пути: ')), input('Станции: '))
        print(csv_file)
    elif comand == '3':
        col = input('Колонка: ')
        val = int(input('Значение: '))
        drop_by_arg(val, col_name=col)
    elif comand == '4':
        print()
    elif comand == '5':
        col = input('Колонка: ')
        val = input('Значение: ')
        find_time(val, col_name=col)
    elif comand == '6':
        col = input('Колонка: ')
        val = int(input('Значение: '))
        station_train(val, col_name=col)
    elif comand == '7':
        print()
    elif comand == '8':
        avg_time()
    elif comand == '9':
        save()
    elif comand == '0':
        print('\n'.join([f"{k} : {v}" for k, v in menu.items()]))
    else:
        break
