# conditional statements allow you to check conditions and run code based on what is true
# if statement checks a condition and runs code if it is true
# else statement runs code if the condition is false
"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("you can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""
# in python indention is really important it is used to define code blocks
# you can either use 4 spaces or a tab
# when writing code under an if or else statement remember to indent
# else statements are optional , you can have an if statement without else
# else statement is used to define what should happen if the condition is false 
# and the if statement is not executed they should always be at the same
# indentation level as the if statement
# the comparison Operators in Python are:
# (>) greater than, (<) less than, (==) equal to, (!=) not equal 
# (>=) greater than or equal to, (<=) less than or equal to
# one = sign is used to assign values to variables
# two == signs are used to compare values
# exercise 1
"""
number = int(input())
if number % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")
"""
# if statements can also be indent to create nested conditions
"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("please pay child fare of $5")
    elif age > 12 and age <= 18:
        print("please pay youth fare of $9")
    else:
        print("you have to pay the adult fare of $12")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""
# this is an example of a nested if/else statement
# elif statements allow you to check for additional conditions if the previous if/else blocks are not true
# here we add an elif statement to check if the age is between 12 and 18 and charge a youth fare
# exercise 2
# this is a BMI calculator that takes height in meters and weight in kg and calculates 
# BMI and interprets the results
"""
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/height**2

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
"""
# exercise 3
# write a program that checks if a year is a leap year or not
"""
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0 and not year % 100 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")

"""
# you can have multiple conditions in an if statement by using logical 
# operators these are AND, OR and NOT
# AND (and) both conditions must be true for the block to execute
# OR (or) if either condition is true the block will execute
# NOT (not) reverses the outcome of a condition
# here is an example of a program that has multiple conditions in the if statement
# you can add multiple conditions using logical operators AND (and), OR (or) and NOT (not)
# you can have multiple if statements on 
# the same indentation level to check different conditions
"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print(" child tickets are $5")
        bill += 5
    elif age > 12 and age <= 18:
        print("youth tickets are $9")
        bill += 9
    else:
        print(" adult tickets are  $12")
        bill += 12
    pic = input("Would you like a photo taken? Y/N ")
    if pic == "Y" or pic == "y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""

# exercise 4
"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")
"""
# this is a modified version of the rollercoaster program that adds 
# an additional condition to check if a person is between 45-55 years old and gives 
# them a free ticket if they are experiencing a midlife crisis
"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print(" child tickets are $5")
        bill += 5
    elif age > 12 and age <= 18:
        print("youth tickets are $9")
        bill += 9
    elif age >= 18:
        if age >= 45 and age > 55:
            print("midlifecrisis tickets are free")
        else:
            print(" adult tickets are  $12")
            bill += 12
    pic = input("Would you like a photo taken? Y/N ")
    if pic == "Y" or pic == "y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""
# exercise 5
# this is a love calculator that takes two names and calculates a love score out of 100
"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
love = ["l", "o", "v", "e",]
combined = name1 + name2
combined_lower = combined.lower()
t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")
true_score =str(t + r + u + e)
l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")
love_score =str(l+o+v+e)
score = true_score + love_score
score_int = int(score)
if score_int <= 10 or score_int >= 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int >= 40 and score_int < 51:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")
"""
# project

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choices_1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
choices_1 = choices_1.lower()
if choices_1 == "left":
    choices_2=input("you arrive at a lake  do you want to wait or swim across ? Type 'wait' or 'swim'")
    choices_2=choices_2.lower()
    if choices_2 == "wait":
        door = input(" which door do you want to go through ? Type 'red', 'yellow' or 'blue'")
        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "red" or door == "blue":
            print("Game Over! You chose the wrong door. Try again.")
    else:
        print("Game Over! You were attacked by trout. Try again.")
    