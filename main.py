import time

balance = 0.0
deposit = 0.0
extract = "EXTRACT".center(30, "#")
withdraw = 0.0
withdraw_limit = 500.0
withdraw_count = 0
WITHDRAW_LIMIT_COUNT = 3

while True:
    menu = f'''
    #####[MENU]#####
    [1] Deposit
    [2] Withdraw
    [3] Check Balance
    [4] View Extract
    [5] Exit

    Select an option: '''
    option = input(menu)
    
    if option == '1':
        print("\n"+"Entering Deposit function.".center(30)+"\n")
        deposit = input("   Enter deposit amount: ")
        try:
            deposit = float(deposit)
            while deposit <= 0:
                print("\n" + "Deposit amount must be positive.".center(30) + "\n")
                deposit = input("   Enter deposit amount: ")
                deposit = float(deposit)
            balance += deposit
            print(f"Deposited: R${deposit:.2f}. New balance: R${balance:.2f}")
            extract += f"\nDeposit: R${deposit:.2f}"
        except ValueError:
            print("\n" + "Invalid input. Please enter a valid number.".center(30) + "\n")
    elif option == '2':
        print("\n"+"Entering Withdraw function.".center(30)+"\n")
        if withdraw_count < WITHDRAW_LIMIT_COUNT:
            withdraw = input("  Enter withdrawal amount: ")
            try:
                withdraw = float(withdraw)
                while withdraw <= 0 or withdraw > balance or withdraw > withdraw_limit:
                    if withdraw <= 0:
                        print("\n" + "Withdrawal amount must be positive.".center(30) + "\n")
                    elif withdraw > balance:
                        print("\n" + "Insufficient balance for this withdrawal.".center(30) + "\n")
                    elif withdraw > withdraw_limit:
                        print("\n" + f"Withdrawal limit is R${withdraw_limit:.2f}.".center(30) + "\n")
                    else:
                        print("\n" + "Unexpected error. Please try again.".center(30) + "\n")
                    withdraw = input("  Enter withdrawal amount: ")
                    withdraw = float(withdraw)
                balance -= withdraw
                withdraw_count += 1
                print(f"Withdrew: R${withdraw:.2f}. New balance: R${balance:.2f}".center(30))
                extract += f"\nWithdrawal: R${withdraw:.2f}"
            except ValueError:
                print("\n" + "Invalid input. Please enter a valid number.".center(30) + "\n")
        else:
            print("\n" + "Withdrawal limit reached. You can only withdraw 3 times per day.".center(30) + "\n")
    elif option == '3':
        print("\n"+"Entering Check Balance function.".center(30)+"\n")
        print(f"Current balance: R${balance:.2f}".center(30))
    elif option == '4':
        print("\n"+"Entering View Extract function.".center(30)+"\n")
        if extract.strip() == "EXTRACT".center(30, "#"):
            print("No transactions to display.".center(30))
        else:
            print(extract)
    elif option == '5':
        print("\n"+"Exiting the menu. Goodbye!".center(30)+"\n")
        time.sleep(1)
        break
    else:
        print("\n" + "Invalid option, please try again.".center(30) + "\n")
    
    time.sleep(1.5)