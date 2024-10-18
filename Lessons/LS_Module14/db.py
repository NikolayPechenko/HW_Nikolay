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

cursor.execute('SELECT username, age FROM Users WHERE age < ?', (35,))
users = cursor.fetchall()  # записали в переменную
for i in users:
    print(i)

connection.commit()
connection.close()