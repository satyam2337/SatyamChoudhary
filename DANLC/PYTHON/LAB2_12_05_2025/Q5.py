p_quantity=int(input("Enter the Purchase quantity: "))
total=p_quantity*100
if p_quantity >= 1000:
    print("you will get 10% discount.")
    D_Price=total-(total*0.1)
    print(f"Total amount is {D_Price}.")
else:
    print("sorry no discount.")
    print(f"Total amount is {total}.")
    

