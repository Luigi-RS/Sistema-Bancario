#MODULES
import time
import os

#VARIABLES
CENTER = 80
clients_all = [
    {
        "name": "joão",
        "cpf": "00000000000"
    }
]
menu = "[MAIN MENU]".center(CENTER, "#")
menu += "\n" + "Welcome to Guará's Bank".center(CENTER) + "\n"
menu = f'''{menu}

        [1] Already a client
        [2] New client
        [3] Exit

        Select an option: '''

#FUNCTIONS
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def deposit(balance, extract,/):
    #VARIABLES
    global CENTER
    deposit_amount = input("   Enter deposit amount: ")

    #CODE
    try:
        deposit_amount = float(deposit_amount)
        while deposit_amount <= 0:
            print("\n" + "Deposit amount must be positive.".center(CENTER) + "\n")
            deposit_amount = input("   Enter deposit amount: ")
            deposit_amount = float(deposit_amount)
        balance += deposit_amount
        print(f"Deposited: R${deposit_amount:.2f}. New balance: R${balance:.2f}")
        extract += f"\nDeposit: R${deposit_amount:.2f}"
    except ValueError:
        print("\n" + "Invalid input. Please enter a valid number.".center(CENTER) + "\n")
    return balance, extract

def withdraw(*, balance, extract, limit, count, LIMIT_COUNT):
    #VARIABLES
    global CENTER

    #CODE
    if count < LIMIT_COUNT:
        withdraw_amount = input("  Enter withdrawal amount: ")
        try:
            withdraw_amount = float(withdraw_amount)
            while withdraw_amount <= 0 or withdraw_amount > balance or withdraw_amount > limit:
                if withdraw_amount <= 0:
                    print("\n" + "Withdrawal amount must be positive.".center(CENTER) + "\n")
                elif withdraw_amount > balance:
                    print("\n" + "Insufficient balance for this withdrawal.".center(CENTER) + "\n")
                elif withdraw_amount > limit:
                    print("\n" + f"Withdrawal limit is R${limit:.2f}.".center(CENTER) + "\n")
                else:
                    print("\n" + "Unexpected error. Please try again.".center(CENTER) + "\n")
                withdraw_amount = input("  Enter withdrawal amount: ")
                withdraw_amount = float(withdraw_amount)
            balance -= withdraw_amount
            count += 1
            print(f"Withdrew: R${withdraw_amount:.2f}. New balance: R${balance:.2f}".center(CENTER))
            extract += f"\nWithdrawal: R${withdraw_amount:.2f}"
        except ValueError:
            print("\n" + "Invalid input. Please enter a valid number.".center(CENTER) + "\n")
    else:
        print("\n" + "Withdrawal limit reached. You can only withdraw 3 times per day.".center(CENTER) + "\n")
    return balance, extract, count

def extraction(balance,/,*, extract):
    #VARIABLES
    global CENTER

    #CODE
    if extract.strip() == "EXTRACT".center(CENTER, "#"):
        print("No transactions to display.".center(CENTER))
    else:
        print(extract)
    input("\nPress Enter to return to the menu.".center(CENTER))
    return extract

def create_client():
    #VARIABLES
    global CENTER, clients_all
    verified = False
    cpf = input("Enter your CPF (only numbers): ").strip()
    while not cpf.isdigit() or len(cpf) != 11:
        print("\n" + "Invalid CPF. Please enter a valid 11-digit CPF.".center(CENTER) + "\n")
        cpf = input("Enter your CPF (only numbers): ").strip()
    while verified == False:  
        for client in clients_all:
            if cpf == client["cpf"]:
                cpf = input("This CPF is already registered, try again or type [e] to return to main menu: ")
                if cpf == "e":
                    return
            else:
                verified = True
    name = input("Enter your first name: ")
    surname = input("Enter your last name: ")
    input("Press Enter to return to the main menu.\n".center(CENTER))

def client_menu():
    #VARIABLES
    global CENTER, clients_all

    #CODE
    account_menu()

#ACCOUNT MENU FUNCTION
def account_menu(balance = 0.0):
    #VARIABLES
    global CENTER, clients_all
    extract = "EXTRACT".center(CENTER, "#")
    withdraw_limit = 500.0
    withdraw_count = 0
    WITHDRAW_LIMIT_COUNT = 3

    #CODE
    while True:
        clear_terminal()
        menu_a = "[MENU]".center(CENTER, "#")
        menu_a = f'''
        {menu_a}

        [1] Deposit
        [2] Withdraw
        [3] Check Balance
        [4] View Extract
        [5] Exit

        Select an option: '''
        option = input(menu_a).strip()
        clear_terminal()
        
        if option == '1':
            print("\n"+"Entering Deposit function.".center(CENTER)+"\n")
            balance, extract = deposit(balance, extract)
        elif option == '2':
            print("\n"+"Entering Withdraw function.".center(CENTER)+"\n")
            balance, extract, withdraw_count = withdraw(balance=balance, extract=extract, limit=withdraw_limit, count=withdraw_count, LIMIT_COUNT=WITHDRAW_LIMIT_COUNT)
        elif option == '3':
            print("\n"+"Entering Check Balance function.".center(CENTER)+"\n")
            print(f"Current balance: R${balance:.2f}".center(CENTER))
            input("\nPress Enter to return to the menu.".center(CENTER))
            clear_terminal()
            continue
        elif option == '4':
            print("\n"+"Entering View Extract function.".center(CENTER)+"\n")
            extract = extraction(balance, extract=extract)
            clear_terminal()
            continue
        elif option == '5':
            print("\n" + "Thanks for visiting us.".center(CENTER) + "\n" + "Goodbye! Have a nice day!".center(CENTER) + "\n")
            time.sleep(1)
            clear_terminal()
            break
        else:
            print("\n" + "Invalid option, please try again.".center(CENTER) + "\n")
        
        time.sleep(1.5)

#CODE
while True:
    clear_terminal()
    option = input(menu).strip()
    clear_terminal()
    if option == '1':
        print("\n" + "Entering Client Menu.".center(CENTER) + "\n")
        client_menu()
        break
    elif option == '2':
        print("\n" + "Entering New Client Menu.".center(CENTER) + "\n")
        create_client()
    else:
        print("\n" + "Thanks for visiting us.".center(CENTER) + "\n" + "Goodbye! Have a nice day!".center(CENTER) + "\n")
        time.sleep(2.5)
        clear_terminal()
        break