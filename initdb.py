import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (stocknumber, registration, vinnumber) VALUES (?, ?, ?)",
            ('145831', 'QAY216', '7AT0C139X21101545')
            )

connection.commit()
connection.close()