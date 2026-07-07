# Calculator Program


# Taking input from the user
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))


# Taking the operation
operation = input("Enter Operation (+, -, *, .) : ")

# Performing the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
     result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        esult = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Invalid Operation"               


# Displaying the result

print("\n========== RESULT ==========")
print("First Number :", num1)
print("Second Number:", num2)
print("Operation    :", operation)
print("Result       :", result)
print("============================")