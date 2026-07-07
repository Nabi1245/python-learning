# Default Parameters

# Pehle ek normal function

# def greet(name):
#     print("Hello", name)

# greet("Nabi")    

# Output = Hello Nabi

# Ab agar tum galti se aise call karo:
#greet()

# To Python error dega.
# TypeError: greet() missing 1 required positional argument: 'name'

# Kyun?

# Kyuki function ko ek parameter (name) chahiye tha, lekin tumne koi value nahi di.


# Is problem ka solution hai Default Parameter

# def greet(name="Guest"):
#     print("Hello", name)

# greet()  

# Output = Hello Guest

# Ab agar value do
# greet("Nabi")

# output = Hello Nabi

# Dry Run

# def greet(name="Guest"):

# Python function ko memory me store karta hai.

# Aur yaad rakhta hai

# name = "Guest"

# Ye default value hai.

# Case 1
# greet()
# Python dekhta hai
# Kya name ki value mili?
# ❌ Nahi.
# Toh woh default use karega.
# name = "Guest"
# Output = Helllo Guest


# Case 2

# greet("Nabi")
# Ab Python dekhta hai
# name = "Nabi"
# Default ignore ho gaya.
# Output = Hello Nabi

# Real Life Example

# Maan lo pizza order karte ho.

def order_pizza(size="Medium"):
    print("Pizza Size:", size)


# Agar customer kuch na bole

order_pizza()  

# Output = Pizza Size: Medium

# Agar bole
# order_pizza("Large")  

# Output = Pizza Size: Large


# Multiple Default Parameters

def student(name="Unknown", city="Mumbai"):
    print(name)
    print(city)


student()    

# Output = Unknown, Mumbai

# Agar

student("Nabi")

# Output = Nabi, Mumbai