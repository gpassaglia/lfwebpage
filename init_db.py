import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO batch (product type, white sugar, brown sugar, lemons, limes, oranges) VALUES (?, ?, ?, ?, "
            "?, ?)",
            ('Pink Lemonade', '120', '1', '2', '3', '4')
            )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
connection.close()