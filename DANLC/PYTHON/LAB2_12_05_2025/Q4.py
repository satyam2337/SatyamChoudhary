salary=int(input("Enter the salary: "))
year=int(input("Enter the year of service: "))

if year > 5:
    bonus=salary*0.05
    print(f"Bonus is {bonus}.")
    print(f"Total salary is {salary + bonus}.")

else:
    print("No bonus.")