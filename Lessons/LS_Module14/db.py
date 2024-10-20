import random
import sqlite3

connection = sqlite3.connect('dat.db')  # подключение к базе данных
cursor = connection.cursor()  # так называемый курсор, необходимый объект
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')  # для обращения к базе данных, позволяет транслировать запросы SQL напрямую в базу данных

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f'newuser{i+1}', f'example{i+1}@gmail.com', random.randint(20, 60)))  # добавление в базу данных

# for i in range(2):  # изменение в базе данных
#     cursor.execute('UPDATE Users SET username = ?, email = ?  WHERE id = ?', (f"newuser{i+1}", f'example{i+1}@gmail.com', i+1))

# cursor.execute('DELETE FROM Users WHERE age > ?', (10,))  # запятая в конце нужна

# cursor.execute('SELECT * FROM Users')  # выбрали все из таблицы

# cursor.execute('SELECT username, age FROM Users WHERE age < ?', (35,))

# cursor.execute('SELECT username, age FROM Users WHERE age < ?', (35,))

# cursor.execute('SELECT SUM(age) FROM Users')
# users = cursor.fetchall()  # записали в переменную.
# for i in users:
#     print(i)

cursor.execute('SELECT SUM(age) FROM Users')
total1 = cursor.fetchone()[0]  # Для выборки из одной строки, позволяет получать конкретный элемент
cursor.execute('SELECT count(age) FROM Users')
total2 = cursor.fetchone()[0]  # перед каждым тоталом новый cursor.execute (запрос)
print(total1/total2 + 1)
cursor.execute('SELECT avg(age) FROM Users')
total3 = cursor.fetchone()[0]
print(total3 + 1)
cursor.execute('SELECT min(age), max(age) FROM Users')
total4 = cursor.fetchone()
print(total4)

connection.commit()
connection.close()