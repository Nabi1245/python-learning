age = int(input("Enter Your Age : "))
has_license = input("Do you have a driving license? (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You Can Drive")
else:
    print("You Cannot Drive")    