# name = "nabi ahmad"
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.lower())

# name = "   Nabi Ahmad   "
# Removes spaces from both sides.
# print(name.strip()). 

# Removes spaces from the left side.
# name = "    Nabi"
# print(name.lstrip())

# Removes spaces from the right side.

# name = "Nabi     "
# print(name.rstrip())

# Replaces one word or character with another.

# text = "I Love Java"

# print(text.replace("Java", "Python"))

# . find()
# Returns the index of the first occurrence.

# text = "Hello Nabi"
# print(text.find("N"))
# print(text.find("x"))

# .index()
# Same as find(), but gives an error if not found.

# text = "Hello"
# print(text.index("H"))
# print(text.index("x"))

# . count()
# Counts how many times a character or word appears.

# text = "banana"

# print(text.count("a"))

# . startswith()

# Checks whether a string starts with a given value.

# text = "Python"

# print(text.startswith("Py"))

# .endswith()
# Checks whether a string ends with a given value.

# text = "Python"

# print(text.endswith("on"))

# . split()
# Converts a string into a list.

# text = "apple mango banana"

# print(text.split())

# date = "01-07-2026"

# print(date.split("-"))

# . join()
# Joins list items into a string.

# fruits = ["Apple", "Banana", "Mango"]

# print(",".join(fruits))

# . isalpha()
# Checks if all characters are alphabets.

# name = "Nabi" 
# print(name.isalpha()) # True

# name = "Nabi124"
# print(name.isalpha()) # False

# . isdigit()
# Checks whether all characters are digits.

# age = "23"

# print(age.isdigit()) # True

# age = "23a"

# print(age.isdigit()) # False

# . isalnum()

# Checks whether a string contains only letters and numbers.

# name = "Nabi123"

# print(name.isalnum()) # True

# text = "Nabi 123"

# print(text.isalnum()) # False

# . islower()

# text = "python"

# print(text.islower()) # True


# text = "Python"

# print(text.islower()) # False

# . isupper()

# text = "PYTHON"

# print(text.isupper()) # True

# . swapcase()

# Changes uppercase to lowercase and lowercase to uppercase.

# text = "pyThOn"

# print(text.swapcase())

# . len()
# Although len() is a built-in function (not a string method), you'll use it constantly with strings.

# name = "Nabi Ahmad"

# print(len(name))

# Real-Life Example

# Suppose the user enters their name with extra spaces:

name = input("Enter your name : ")

clean_name = name.strip().title()

print("Welcom,", clean_name)