# if condition ager True ho jati hai toh python uske under ke code ko read karega aur print karega 
# if conditon ager false ho jati hai toh if ke ander ke code ke python skip kar deta hai aur if ke bahar aa jata hai aur next line ko read karta hai aur print 

# salary = 30000

# if salary >= 25000:
#     print("Congratulations!")
#     print("You are eligible.")

# print("Thank you.")

# 1.
# marks = 20

# if marks >= 35:
#     print("Pass")
# else:
#     print("Fail")

# print("Program End")

# Answer :  Faiil or prgram End because of 20 >= 35 it's False or else wala code chalega ager False condition ho gayi toh 

# 2.

# marks = 90

# if marks >= 35:
#     print("Pass")
# else:
#     print("Fail")

# print("Done")

# Answer :  pass and done because of 90 >= 35 it's true and code excute 

# 3.

# marks = 15

# if marks >= 35:
#     print("Pass")
# else:
#     print("Fail")

# print("Done")

# Answer :  Faiil or Done because of 15 >= 35 it's False or else wala code chalega ager False condition ho gayi toh

# 1.
# age = 25

# if age >= 18:
#     print("Adult")
#     print("Can Vote")
# else:
#     print("Minor")
#     print("Cannot Vote")

# print("Thank You")


# Answer = Adult , Can Vote, Thank You, ->  kyon ki age = 25 or condition 25 >= 18 = True toh print hoga if ke under ka element else wala block skip ho jayega aur end wala print hoga

# 2.
# age = 12

# if age >= 18:
#     print("Adult")
#     print("Can Vote")
# else:
#     print("Minor")
#     print("Cannot Vote")

# print("Thank You")

# Answer = Minor , Cannot Vote, Thank You, ->  kyon ki age = 12 or condition 12 >= 18 = false toh print hoga else ke under ka element

# 3.

# marks = 80

# if marks >= 35:
#     print("Pass")

# print("Hello")

# print("Python")

# Answer = Pass, Hello, Python -> kyon ki 80 >= 35 its True if ke ander ka block pura print hoga 

# 4.

# marks = 75

# if marks >= 90:
#     print("Grade A+")

# elif marks >= 75:
#     print("Grade A")

# elif marks >= 60:
#     print("Grade B")

# else:
#     print("Fail")

# Answer = Grade A -> conditon 75 >= 90 False 75 >= 75 True print code or 60 ke niche fail 


# 1.

# number = 55

# if number > 100:
#     print("A")

# elif number > 80:
#     print("B")

# elif number > 50:
#     print("C")

# elif number > 20:
#     print("D")

# else:
#     print("E")

# print("Finished")

# Answer = C, or Finished Reason: ->  55 > 100 = False next check 55 > 80 = False next check 55 > 50 = True Stop And print code and bahar if conditon and print nixt line finished

# age = 22
# has_id = True

# 2.

# if age >= 18 and has_id:
#     print("Entry Allowed")
# else:
#     print("Entry Denied")

# age = int(input("Enter age:"))

# if age < 0:
#     print("Invalid Age")
# if age < 18:
#     print("you are minor")
# elif age <= 59:
#     print("You Are Adult")
# elif age >= 60:
#     print("You Are Senior Citizen")
# else:
#     print("Sorry Incorrect")


age = int(input("Enter your age : "))

if age <= 0:
    print("Invalid Age")
elif age < 18:
    print("You are Minor")
elif age < 60:
    print("You are Adult")
else:
    print("You are Senior Citizen")            