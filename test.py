import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

users = [(1, 'shreyas', '12345'), (2, 'mahen', '123456'), (3, 'harath', '1234567'), (4, 'aravind', '12345678'), (5, 'naveen', 123456789)]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)
connection.commit()
connection.close()
