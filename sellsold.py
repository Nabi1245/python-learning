# phone qoute check and Budget Phone check

phone = int(input("Enter Your Budget Price : "))

if phone < 20000:
    print("Budget Phone ")
elif phone < 50000:
    print("Mid Range Phone")    
else:
    print("Premium Phone")

print("Are You Agree ")



age = int(input("Enter Age: "))
has_license = input("Do you have a driving license? (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You can drive.")
else:
    print("You cannot drive.")