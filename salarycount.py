salary = int(input("Enter your salary : "))

if salary <= 0:
    print("Invalid Salary")
elif salary < 10000:
    print("Low Salary")

elif salary < 50000:
    print("Medium Salary")    

else:
    print("High Salary")