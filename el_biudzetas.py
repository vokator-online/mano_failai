def income(income, ammount, transactions):
    transactions[income] = abs(float(ammount))
    return transactions
   
def expense(expenses, ammount, transactions):
    transactions[expenses] = -abs(float(ammount))
    return transactions  
 
transactions = {}

while True:
    print("""
    |Hello, please choose an operation|

1 - add income
2 - add expense
3 - show transactions
4 - show budget

0 - exit
""")

    choice = input("Enter a number: ")
    if choice.startswith('0'):
        print("Thank you for choosing us and have a nice day!")
        break
    elif choice.startswith('1'):
        incomes = input("Please enter a income: ")
        ammount = input("Please enter the ammount of the income: ")
        transactions = income(incomes, ammount, transactions)
    elif choice.startswith('2'):
        expenses = input("Please enter a expense: ")
        ammount = input("Please enter the ammount of the expense: ")
        transactions = expense(expenses, ammount, transactions)
    elif choice.startswith('3'):
        print("Your transactions are:")
        for key, value in transactions.items():
            print(f"""{key}  {value}""") 
    elif choice.startswith('4'):
        print(sum(transactions.values()))