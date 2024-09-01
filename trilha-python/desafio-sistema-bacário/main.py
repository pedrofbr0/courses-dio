def display_menu():
    menu = """
    [d] Deposit
    [w] Withdraw
    [s] Statement
    [q] Quit

    => """
    return input(menu).lower()

def deposit(balance, statement):
    amount = float(input("Enter the deposit amount: "))
    if amount > 0:
        balance += amount
        statement += f"Deposit: ${amount:.2f}\n"
        print("Deposit successful!")
    else:
        print("Operation failed! The entered amount is invalid.")
    return balance, statement

def withdraw(balance, statement, num_withdrawals, WITHDRAWAL_LIMIT, limit):
    amount = float(input("Enter the withdrawal amount: "))
    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdrawals = num_withdrawals >= WITHDRAWAL_LIMIT

    if exceeded_balance:
        print("Operation failed! You do not have enough balance.")
    elif exceeded_limit:
        print("Operation failed! The withdrawal amount exceeds the limit.")
    elif exceeded_withdrawals:
        print("Operation failed! Maximum number of withdrawals exceeded.")
    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal: ${amount:.2f}\n"
        num_withdrawals += 1
        print("Withdrawal successful!")
    else:
        print("Operation failed! The entered amount is invalid.")
    
    return balance, statement, num_withdrawals

def display_statement(balance, statement):
    print("\n================ STATEMENT ================")
    print("No transactions made." if not statement else statement)
    print(f"\nBalance: ${balance:.2f}")
    print("===========================================")

def main():
    balance = 0
    limit = 500
    statement = ""
    num_withdrawals = 0
    WITHDRAWAL_LIMIT = 3

    while True:
        option = display_menu()

        if option == "d":
            balance, statement = deposit(balance, statement)
        elif option == "w":
            balance, statement, num_withdrawals = withdraw(balance, statement, num_withdrawals, WITHDRAWAL_LIMIT, limit)
        elif option == "s":
            display_statement(balance, statement)
        elif option == "q":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid operation, please select the desired operation again.")

if __name__ == "__main__":
    main()
