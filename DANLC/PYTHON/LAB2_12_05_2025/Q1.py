balance=float(input("Enter your balance: "))
amount=float(input("Enter the amount to withdraw: "))
if amount <= balance and amount % 100 == 0:
    print(f"Transaction successful. {amount} withdrawn.")
    balance -= amount
    print(f"New balance: {balance}")
else:
    if amount > balance:
        print("Insufficient funds.")
    else:
        print("Amount should be a multiple of 100.")
            
       



