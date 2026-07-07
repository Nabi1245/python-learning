'''
Typecasting Kya Hota Hai?

Definition:

Simple language mein:


Typecasting ka matlab hota hai ek data type ko dusre data type mein convert karna.

Agar kisi value ka type change karna ho, us process ko Typecasting kehte hain.

'''

# Example 1 (Without Typecasting)
# num = input("Enter a number : ")
# print(type(num)) # out put string 

# Problem Without Typecasting

# num1 = input("Enter first number : ")
# num2 = input("Enter second number : ")

# print(num1 + num2)




# Example 2 (With Typecasting)
# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# print(num3 + num4)

# price = float("99.99")
# print(price)
# print(type(price))

# age = 22

# age = str(age)

# print(age)
# print(type(age))


# bool() Typecasting

# print(bool(1))
# print(bool(0))
# print(bool(""))
# print(bool("Hello"))

# 0 → False

# Baaki Numbers → True

# "" (empty string) → False

# Koi bhi text → True

quantity = int(input("Enter Quantity : "))
price = 500
total = quantity * price
print("The Final Quantity : ",total) 