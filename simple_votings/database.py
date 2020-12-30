import sqlite3


def db_create():  # Создание БД
    # Проверка на наличие БД
    try:
        open('data.db')
    except FileNotFoundError:
        # Подключение БД
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Создание таблиц
        cursor.execute('CREATE TABLE Users\n'  # Таблица Users, 8 полей
                       '('
                       'id integer,'  # ID пользователя - число
                       'name text,'  # Имя
                       'email text,'  # E-mail
                       'pass text,'  # Пароль
                       'role integer,'  # Роль (0 - обычный, 1 - админ)
                       'polls_create text,'  # Созданные пользователем голосования
                       'polls_voted text,'  # ???
                       'photo text'  # Путь к фото профиля
                       ')\n')
        cursor.execute('CREATE TABLE Polls\n'  # Таблица Polls, 7 полей
                       '('
                       'id integer,'  # ID голосования - число
                       'type text,'  # Тип чего???
                       'name text,'  # Имя
                       'variants text,'  # Варианты ответов
                       'choose_type text,'  # ???
                       'color text,'  # Цвет
                       'back_ground_image text)'  # Фоновая картинка
                       '\n')


def db_insert(table: str, args: list[tuple]):  # Вставка в БД
    # Подключение БД
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Вставляем данные в таблицу
    cursor.executemany(f'INSERT INTO {table} VALUES ({"?, " * (len(args[0]) - 1)}?)', args)

    # Сохраняем изменения
    conn.commit()


def db_change(table: str, field: str, record, change_to):  # Замена одной записи на другую
    # Подключение БД
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Замена записей
    cursor.execute(f"UPDATE {table}\n"
                   f"SET {field} = '{change_to}'\n"
                   f"WHERE {field} = '{record}'\n")

    # Сохраняем изменения
    conn.commit()


def db_delete(table: str, field: str, record):  # Удаление записи
    # Подключение БД
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Удаление записей
    cursor.execute(f'DELETE FROM {table}\n'
                   f'WHERE {field} = {record}')

    # Сохраняем изменения
    conn.commit()


def db_exec(command: str, args=None):  # Выделение элементов
    # Подключение БД
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    # Проверка на наличие аргументов
    if args is None:
        cursor.execute(command)
    else:
        cursor.execute(command, args)

    # Сохраняем изменения
    conn.commit()

    # Возврат возможного значения
    return cursor.fetchall()
