import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')


# def create_con():
#     con = sqlite3.connect('data.db')


def get_all_products():
    with connection:
        cursor.execute('SELECT * FROM Products')
        all_products = cursor.fetchall()
        return all_products


all = get_all_products()


# def add_user(username, email, age):
#     con = sqlite3.connect('data.db')
#     cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
#     connection.commit()
#     con.close()


def add_user(username, email, age):
    with connection:
        cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
        connection.commit()


# def is_included(username):
#     con = sqlite3.connect('data.db')
#     inc = cursor.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchone()
#     if inc is not None:
#         con.commit()
#         con.close()
#         return True
#     else:
#         con.commit()
#         con.close()
#         return False


def is_included(username):
    with connection:
        inc = cursor.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchone()
        if inc is not None:
            connection.commit()
            return True
        else:
            connection.commit()
            return False


if __name__ == '__main__':
    connection.commit()
    connection.close()



