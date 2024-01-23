import pickle

def load_transactions():
    try:
        with open('transactions.pickle', 'rb') as file:
            transactions = pickle.load(file)
    except (FileNotFoundError, EOFError):
        transactions = {}
    return transactions

def save_transactions(transactions):
    with open('transactions.pickle', 'wb') as file:
        pickle.dump(transactions, file)

# Pakeitimai funkcijose income ir expense, kad būtų išsaugoma ir atnaujinama informacija
def income(income, amount, transactions):
    transactions[income] = abs(float(amount))
    save_transactions(transactions)
    return transactions

def expense(expense, amount, transactions):
    transactions[expense] = -abs(float(amount))
    save_transactions(transactions)
    return transactions

# Pradinė transakcijų įkėlimo vieta
transactions = load_transactions()

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
        save_transactions(transactions)  # Išsaugojame transakcijas prieš baigiant programą
        break
    elif choice.startswith('1'):
        incomes = input("Please enter an income: ")
        amount = input("Please enter the amount of the income: ")
        transactions = income(incomes, amount, transactions)
    elif choice.startswith('2'):
        expenses = input("Please enter an expense: ")
        amount = input("Please enter the amount of the expense: ")
        transactions = expense(expenses, amount, transactions)
    elif choice.startswith('3'):
        print("Your transactions are:")
        for key, value in transactions.items():
            print(f"""{key}  {value}""")
    elif choice.startswith('4'):
        print(sum(transactions.values()))