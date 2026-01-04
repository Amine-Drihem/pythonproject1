
def show_balance(balance):
    print(f"your balance is {balance:.2f}$")


def deposit():
    amount = float(input("enter amount to deposit: "))
    if amount < 0:
        print("that amount is not valid")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to withdraw: "))
    if amount > balance:
        print("insufficient fund")
        return 0
    elif amount < 0:
        print("amount should be positive")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("banking program")
        print("")
        print("1- show balance")
        print("2- deposit")
        print("3- withdraw")
        print("4- exit")
        choice = input("Enter your choice (1 to 4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("that choice is not valid")

    print("thank you have a nice day")

if __name__ == '__main__':
    main()
