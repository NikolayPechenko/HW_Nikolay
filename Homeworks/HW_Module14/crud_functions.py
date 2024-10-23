import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    return all_products


all = get_all_products()


# cursor.execute("INSERT INTO Users (title, description, price) VALUES ('Product1', 'beauty', 100)")
# cursor.execute("INSERT INTO Users (title, description, price) VALUES ('Product2', 'Collagen', 200)")
# cursor.execute("INSERT INTO Users (title, description, price) VALUES ('Product3', 'D3', 300)")
# cursor.execute("INSERT INTO Users (title, description, price) VALUES ('Product4', 'Omega', 400)")

connection.commit()
connection.close()