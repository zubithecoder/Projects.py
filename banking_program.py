# Making a Banking Program Using Only Python

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}") # :.2f shows 2 decimal places after the point

def deposit():
    amount = float(input("Enter amount to deposit: $"))

    if amount < 0:
        print("That is not a valid amount.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        return amount 
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n*********************************")
        print("Welcome to the Banking Program")
        print("*********************************")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit") 
        print("*********************************")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("*************************************************")
            print("Thank you for using the Banking Program. Goodbye!")
            print("*************************************************")
        else:
            print("*********************************")
            print("Invalid choice. Please try again.") 
            print("*********************************")

if __name__ == "__main__":
    main()
