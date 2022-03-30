import sqlite3 as sql
import matplotlib.pyplot as plt
import numpy as np

def All_Transactions():
    conn = sql.connect(r'./Data.db')
    cursor = conn.cursor()
    for row in cursor.execute('SELECT * FROM Transactions'):
        head = list(row)
        if head[0] == 0:
            print(head)
        else:
            print(row)


def Total_Expenses():
    conn = sql.connect(r'./Data.db')

    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE Total (Total_Amount INT DEFAULT 0, Count INT)")
        cursor.commit()
    except:
        pass
    
    cursor.execute('SELECT Count FROM Total')
    validate = str(cursor.fetchone())
    validate = validate[1]
    #print (validate)

    if int(validate) != 1: 
        cursor.execute("INSERT INTO Total VALUES(0,1)")
        conn.commit()
    
    else:
        pass

    
    cursor.execute('SELECT SUM(Amount) FROM Transactions')
    price = list(cursor.fetchone())
    return price


def New_Expense(amount, description, method):
    conn = sql.connect(r'./Data.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Transactions(Amount,Description,Method) VALUES(?,?,?)", (amount,description,method))
    conn.commit()
    Total_Transactions()



def Total_Transactions():
    conn = sql.connect(r'./Data.db')

    cursor = conn.cursor()

    cursor.execute('SELECT SUM(Amount) FROM Transactions WHERE Transaction_Number != 0')
    price = list(cursor.fetchone())

    cursor.execute('UPDATE Total SET Total_Amount = ?',(price))
    conn.commit()

    total = int(price[0])
    return (total)



def Delete_Transaction(number):
    conn = sql.connect(r'./Data.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM Transactions WHERE Transaction_Number = ?',(str(number)))
    conn.commit()
    All_Transactions()

def View_Chart():
    conn = sql.connect(r'./Data.db')
    cursor = conn.cursor()
    
    amounts=[]
    for price in cursor.execute('SELECT Amount FROM Transactions'):
        amounts.append(int(price[0]))

    labels=[]
    for name in cursor.execute('SELECT Description FROM Transactions'):
        labels.append(str(name[0]))

    amounts = list(amounts)

    if (len(amounts)>=1 or len(labels)>=1):
        y = np.array(amounts)
        x = np.array(labels)

        plt.pie(y, labels=labels, autopct='%.0f%%')
        plt.show()
    
    elif(len(amounts)==0 or len(name)==0):
        print("Chart unable to generate")

