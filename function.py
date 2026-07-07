# def nabi():
#     print("Helllo")

# nabi()


# Example 1

# def say_hello(name):
#     print("Hello {name}, How Are You ? ")

# say_hello("Nabi")
# say_hello("Ismail")
# say_hello("Ahmad")
# say_hello("Arman")


# def add_numbers(a, b):
#     sum_result = a + b
#     return sum_result  # Yeh value waapas bhej raha hai

# # Function ko call kiya aur uska result ek variable mein save kiya
# output = add_numbers(10, 20)

# print("Dono numbers ka sum hai:", output)

# def add(a,b):
#     sumData = a + b
#     return sumData


# output = [
#     add(10, 20),
#     add(10, 30),
#     add(10, 50),
#     add(10, 70),
#     add(10, 90),
#     add(10, 100),
#     add(10, 200),
# ]    

# Loop through and print each stored value

# for haroon in output:
#     print("The Value is :",haroon)

# output = add(10,20)     
# output = add(10,30)     
# output = add(10,50)     
# output = add(10,70)     
# output = add(10,90)
# output = add(100,100)

# print("The Value is : ", output)


# Without return
# def add(a, b):
#     print(a + b)

# x = add(10, 30)

# print(x)


# with return 

def add(a, b):
    return a + b


x = add(10, 40)

print(x)