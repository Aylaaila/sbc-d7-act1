import random

acc = {}

def genacc():
    return str(random.randint(10000, 99999))

def create(accnum=None):
    if not accnum:
        accnum = genacc()
        while accnum in acc:
            accnum = genacc()
    elif accnum in acc:
        return None, "Account already exists."

    acc[accnum] = {'balance': 1000}
    return accnum, "Account created successfully."

def check(accnum):
    return acc.get(accnum, {}).get('balance', "Account not found.")

def deposit(accnum, amount):
    if accnum in acc and amount > 0:
        acc[accnum]['balance'] += amount
        return f"Deposited {amount}. New balance: {acc[accnum]['balance']}"
    return "Invalid account or deposit amount."

def withdraw(accnum, amount):
    if accnum in acc and amount > 0:
        if acc[accnum]['balance'] >= amount:
            acc[accnum]['balance'] -= amount
            return f"Withdrew {amount}. New balance: {acc[accnum]['balance']}"
        return "Insufficient funds."
    return "Invalid account or withdrawal amount."

def delacc(accnum):
    if accnum in acc:
        del acc[accnum]
        return "Account deleted."
    return "Account not found."

def show_menu():
    print("\nMy Bank")
    print("CA - Create Account")
    print("CB - Check Balance")
    print(" D - Deposit")
    print(" W - Withdraw")
    print("DA - Delete Account")
    print(" E - Exit")
    return input("Enter your choice: ")

def get(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer!")

while True:
    choice = show_menu()
    
    if choice == 'CA':
        while True:
            user_id = get("New account number: ")
            account_id, message = create(str(user_id) if str(user_id) not in acc else None)
            if account_id:
                print(f"Account number: {user_id}")
                break
            else:
                print(message)
    
    elif choice in {'CB', 'D', 'W', 'DA'}:
        accnum = get("Account number: ")
        
        if choice == 'CB':
            print(f"Balance: {check(str(accnum))}")
        
        elif choice == 'D':
            amount = get("Amount to deposit: ")
            print(deposit(str(accnum), amount))
        
        elif choice == 'W':
            amount = get("Amount to withdraw: ")
            print(withdraw(str(accnum), amount))
        
        elif choice == 'DA':
            print(delacc(str(accnum)))
    
    elif choice == 'E':
        print("Exit.")
        break
    
    else:
        print("Invalid.")