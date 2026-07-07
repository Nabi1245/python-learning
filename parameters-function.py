# Sabse pehle code

# def add(a, b):
#     return a + b

# result = add(10, 20)

# print(result)

# Output: 30


# Isme Parameter kya hai?

# 👉 Parameters hain. def add(a, b):

# Definition:

# Function banate waqt brackets () ke andar jo variables likhte hain, unhe Parameters kehte hain.

# Example:

# def student(name, age):
#     pass

# Yahan

# name → Parameter
# age → Parameter

# Argument kya hai?

# 👉 Arguments hain. add(10, 20)

# Definition:
# Jab function ko call karte hain aur actual values dete hain, unhe Arguments kehte hain.

# Dry Run

# def add(a, b):
#     return a + b


# Abhi function sirf memory me save hua.

# Phir

# add(10, 20)

# Python karta hai:

# a = 10
# b = 20

# Ab function ke andar code chal raha hai.

# return a + b

# return 10 + 20

# return 30

# Ab
# result = 30
# Phir
# print(result)
# Output =. 30

# Real Life Example

# Socho pizza order karte ho.

def make_pizza(size, topping):
    print("Size = ",size)
    print("Topping = ",topping)

# Yahan
#    size
#    topping 
# Parameters hain.   

# Call karte ho

make_pizza("Large", "Cheese")    

# To

# size = "Large"
# topping = "Cheese"

# Output

# Large
# Cheese


# Aur Example

def introduce(name, city):
    print("Name :", name)
    print("City :", city)

introduce("Nabi", "Mumbai")

# Dry Run

# name = "Nabi"
# city = "Mumbai"

# output

# Name : "Nabi"
# City : "Mumbai"

# Yaad Rakhne ka Trick

# Function banate waqt
#         ↓
# Parameters

# Function chalate waqt
#         ↓
# Arguments