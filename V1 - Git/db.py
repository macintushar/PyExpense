import sqlite3 as sql

conn = sql.connect(r'path/to/database.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE Transactions (Transaction_Number INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp DATE DEFAULT (datetime('now','localtime')), Amount INT, Description TEXT, Method TEXT)")
conn.commit()
print("Your Wallet has been created!")

for row in cursor.execute('SELECT * FROM Transactions'):
        print(row)


cursor.execute("CREATE TABLE Total (Total_Amount INT DEFAULT 0, Count INT)")
conn.commit()
print("Total amount has been created")

cursor.execute("INSERT INTO Total VALUES(0,1)")
conn.commit()

row = cursor.execute('SELECT * FROM Total')
print(cursor.fetchone())

