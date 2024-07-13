import sys
from bank_account import BankAccount

def print_usage():
    print("Usage:")
    print("python main-0.py <operation> <amount>")
    print("Operations: deposit, withdraw, balance")
    print("Example: python main-0.py deposit 100")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    account = BankAccount()
    operation = sys.argv[1].lower()

    if operation == "balance":
        account.display_balance()
    elif operation in ["deposit", "withdraw"]:
        if len(sys.argv) != 3:
            print_usage()
            return
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Error: Amount must be a number")
            return

        if operation == "deposit":
            if account.deposit(amount):
                print(f"Deposited ${amount:.2f}")
            else:
                print("Invalid deposit amount")
        else:  # withdraw
            if account.withdraw(amount):
                print(f"Withdrawn ${amount:.2f}")
            else:
                print("Insufficient funds or invalid withdrawal amount")
        
        account.display_balance()
    else:
        print_usage()

if __name__ == "__main__":
    main()