import random
import sqlite3

connection = sqlite3.connect('db.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER,
username TEXT,
first_name TEXT,
block INTEGER
);
''')


def add_user(user_id, username, first_name):
    check_user = cursor.execute('SELECT * FROM Users WHERE id = user_id')
    if check_user.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Users VALUES ('{user_id}','{username}','{first_name}', 0)
    ''')
    connection.commit()


def show_users():
    user_list = cursor.execute('SELECT * FROM Users').fetchall()
    message = ''
    for i in user_list:
        message += f'{i[0]} @{i[1]} {i[2]} \n'
    connection.commit()
    return message


def show_stat():
    count_users = cursor.execute('SELECT COUNT(*) FROM Users').fetchone()
    connection.commit()
    return count_users[0]


def add_to_block(input_id):
    cursor.execute(f'UPDATE Users SET block = 1 WHERE id = {input_id}')
    connection.commit()


def check_block(user_id):
    users = cursor.execute(f'SELECT block FROM Users WHERE id = {user_id}').fetchone()
    connection.commit()
    return users


def unblock(input_id):
    cursor.execute(f'UPDATE Users SET block = 0 WHERE id = {input_id}')
    connection.commit()


connection.commit()
connection.close()