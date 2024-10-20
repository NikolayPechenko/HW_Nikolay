import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f'User{i + 1}', f'example{i + 1}@gmail.com', (i+1) * 10, 1000))
#
# cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 > ?', (0,))
#
# cursor.execute('DELETE FROM Users WHERE id % 3 = ?', (1,))
#
# cursor.execute('DELETE FROM Users WHERE id > 10')

# cursor.execute('SELECT * FROM Users WHERE age <> ?', (60,))
# users = cursor.fetchall()
# for i in users:
#     print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT Count(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT Sum(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()
