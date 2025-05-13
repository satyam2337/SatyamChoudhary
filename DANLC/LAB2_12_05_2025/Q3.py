p_amount=int(input("Enter the Purchase amount: "))
if p_amount >= 500:
    print("Shipping is free.")

else:
    print("Shipping is 50.")
    total=p_amount+50
print(f"Total amount is {total}.")