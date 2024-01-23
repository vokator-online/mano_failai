def add_income(income, amount): # zodis def pranesa, kad mes aprasysime funkcija, siuo atveju add_income yra funcijos pavadinimas; skliaustuose bus kintamieji kuriuos naudojame funkcijos viduje, kad gautume atsakyma apie income 
    income += amount # x = x + y; dar kitaip butu income = income + amount
    print(f"Income added: {amount}") # tada printinam savo f(funkcija) su tekstu ir lauztiniuose skliaustuose nurodome kieki (amount) kuri norime skaiciuoti 
    return income # return vartotojo sasajoje grazina musu esama income, kai vartotojo sasajoje mes ivedama (amount) t.y kieki ir mes pamatome koks buvo musu income 

def add_expense(expenses, amount): # zodis def pranesa, kad mes aprasysime funkcija, siuo atveju add_expense yra funcijos pavadinimas; skliaustuose bus kintamieji kuriuos naudojame funkcijos viduje, kad gautume atsakyma apie expenses
    expenses += amount # x = x + y; dar kitaip butu expenses = expenses + amount
    print(f"Expense added: {amount}") # tada printinam savo f(funkcija) su tekstu ir lauztiniuose skliaustuose nurodome kieki (amount) kuri norime skaiciuoti 
    return expenses # return vartotojo sasajoje grazina musu esamus expenses, kai vartotojo sasajoje mes ivedama (amount) t.y kieki ir mes pamatome koks buvo musu expense 

def calculate_balance(income, expenses): # zodis def pranesa, kad mes aprasysime funkcija, siuo atveju calculate_balance yra funkcijos pavadinimas; skliaustuose yra kintamieji kuriuos naudojame funkcijos viduje kad suzinotume savo balansa
    balance = income - expenses # z = x - y; dar kitaip butu balancas = income - expenses
    print(f"Current balance: {balance}") # sitas f stringas isprintina musu 'Z' t.y, balansa 

# User Interface
income = 0 # sitoje vietoje income priskiriame kintamajam ir ta kintamaji priskiriame 0. Programavime tai yra įprasta praktika priskirti pradinę reikšmę kintamajam prieš jį naudojant skaičiavimuose ar kitose operacijose. Šiuo atveju pradedama nuo pradinio nulio pajamų, o vėliau galite šį kintamąjį atnaujinti ar modifikuoti pagal poreikį jūsų programoje.
expenses = 0 # # sitoje vietoje expenses priskiriame kintamajam ir ta kintamaji priskiriame 0. Programavime tai yra įprasta praktika priskirti pradinę reikšmę kintamajam prieš jį naudojant skaičiavimuose ar kitose operacijose. Šiuo atveju pradedama nuo pradinio nulio islaidu, o vėliau galite šį kintamąjį atnaujinti ar modifikuoti pagal poreikį jūsų programoje.

while True: # sukuria begalinį ciklą, ir jame yra seka print komandų, kurios rodo įvairias galimybes vartotojui (siuo metu 4 ivesties galimybes).
    print("\nOptions:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ") # tada naudoja input funkciją, kad užfiksuotų įvestį. Įvesta reikšmė bus saugoma kintamajame choice. Tai dažnai naudojama meniu valdomuose programuose, kur vartotojas turi įvesti skaitinį pasirinkimą, atitinkantį anksčiau pateiktas galimybes.

    if choice == '1': # jeigu vartotojas pasirenka '1'(du lygybes zenklai tikrina ar tai yra tiesa, siuo metu ar choice (pasirinkimas) yra atitinkamas 1 (t.y pasirinkimui vienetas))
        amount = float(input("Enter the income amount: ")) # sitoje vietoje yra paprasoma vartotojo ivesti savo amount (kieki) kuri jis nori prideti prie savo income. Float funkcija naudojama, kad paverstu vartotojo ivesta teksta i skaiciu kuris rodytu skaiciu per kableli. Todel naudojama float funkcija su skliaustais ir viduje irasome input ' float(input(ir tekstas viduje-kuris pavirs skaiciu, per kableli))'' Input funkcija atlieka tai, kad uzfiksuotu vartotojo ivesti. 
        income = add_income(income, amount) # cia yra iskvieciama komanda add_income, kuri atlieka sudeti tarp income ir amount. 
    elif choice == '2': # jeigu vartotojas pasirenka '2' ((du lygybes zenklai tikrina ar tai yra tiesa, siuo metu ar choice (pasirinkimas) yra atitinkamas 2 (t.y pasirinkimui dvejetas))
        amount = float(input("Enter the expense amount: ")) # sitoje vietoje yra paprasoma vartotojo ivesti savo amount (kieki) kuri jis nori prideti prie savo expense. Float funkcija naudojama, kad paverstu vartotojo ivesta teksta i skaiciu kuris rodytu skaiciu per kableli. Todel naudojama float funkcija su skliaustais ir viduje irasome input ' float(input(ir tekstas viduje-kuris pavirs skaiciu, per kableli))'' Input funkcija atlieka tai, kad uzfiksuotu vartotojo ivesti. 
        expenses = add_expense(expenses, amount) #cia yra iskvieciama komanda add_expense, kuri atlieka sudeti tarp expense ir amount. 
    elif choice == '3': # jeigu vartotojas pasirenka '3' ((du lygybes zenklai tikrina ar tai yra tiesa, siuo metu ar choice (pasirinkimas) yra atitinkamas 3 (t.y pasirinkimui trejetas)
        calculate_balance(income, expenses) # kad vartotojui parodytu jo balansa yra iskvieciama funkcija calculate_balance kuri daro matematini veikma, kuris is pajamu atima islaidas t.y income - expenses.  
    elif choice == '4': # jeigu vartotojas pasirenka '4' ((du lygybes zenklai tikrina ar tai yra tiesa, siuo metu ar choice (pasirinkimas) yra atitinkamas 4 (t.y pasirinkimui ketvertas)
        print("Exiting the budget calculator. Goodbye!") # vartotojas iveda skaiciu '4' ir tada is iseina is programos
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.") # jeigu vartotojas iveda kitoki skaiciu kuris yra ne ivesties galimybese, jo paprasoma ivesti tinkama skaiciu. 