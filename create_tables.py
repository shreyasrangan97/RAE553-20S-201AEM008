import sqlite3

connection = sqlite3.connect('data.db') #establishing connection for creating data.db

cursor = connection.cursor() #SQL command is created using cursor object by calling execute command.


#TABLE is added for users
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
#TABLE is Added for item
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)
#data included using test item.
cursor.execute("INSERT INTO items VALUES ('hello', '123456789')")

connection.commit() # changes are committed and closed.
connection.close()
