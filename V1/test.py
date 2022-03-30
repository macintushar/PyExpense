import sqlite3 as sql

conn = sql.connect(r'C:\Projects\Expense Manager\V1\Data.db')
cursor = conn.cursor()

'''for row in cursor.execute('SELECT * FROM Transactions'):
    print(row)
    print()


for row in cursor.execute('SELECT * FROM Transactions'):
    head = list(row)
    if head[0] == 0:
        print(head)
    else:
        print(row)


cursor.execute('DELETE FROM Transactions WHERE Transaction_Number = ?', str(3))
conn.commit()
'''
amounts=[]
for price in cursor.execute('SELECT Amount FROM Transactions'):
    amounts.append(int(price[0]))

labels=[]
for name in cursor.execute('SELECT Description FROM Transactions'):
    labels.append(str(name[0]))

amounts = list(amounts)
import matplotlib.pyplot as plt
import numpy as np

y = np.array(amounts)
x = np.array(name)

plt.pie(y, labels=labels, autopct='%.0f%%')
plt.show()