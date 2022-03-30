from db_functions import *

i=0
c=0

while i==0:
    print("\n\nHello! Welcome to Expense Manager\n")
    print("Your Current Expenditure = ", Total_Expenses()[0])
    print("\nMenu options: \n 1. Enter an expense \n 2. View a chart of your expenses \n 3. Show every transaction \n 4. Delete a transaction \n 5. Exit")
    choice = int(input("\nEnter the Option: "))

    if choice == 1:
        amt = int(input("\nEnter the Amount spent: "))
        desc = str(input("\nEnter a Description: "))
        method = str(input("\nEnter the Payment Method: "))
        New_Expense(amount=amt, description=desc, method=method)

    if choice == 2:
        View_Chart()

    if choice == 3:
        All_Transactions()
    
    if choice == 4:
        print()
        All_Transactions()
        no = int(input("\nEnter the Transaction Number to delete: "))
        print()
        Delete_Transaction(number=no)
    
    if choice == 5:
        break

    elif choice == 0 or choice>5:
        print("\nInvalid Input! \n")


