# day 2 of python
# there are different data types in python like strings, integers, floats, booleans
# strings
"""
print("Hello"[-1])
"""
# this is called indexing and allows you to access individual characters in a string
# even tho you can you can put a number in a string , it will still be a string data type and won't be seen as a number
"""
print("123" + "456")
"""
# to convert a string to a number use int() or float()
# int() converts to an integer
#integer
"""
print(123 +345)
"""
# this will actually be calculated as an integer instead of concatenated like strings
# an integer is a whole number
# float is a number with decimal places
# large numbers in python use scientific notation or _
# Float
"""
print(3.14159)
"""
# boolean
# this can only be true or False
# some function can only be used by a certain data type
# len(1234) won't it work as len() only works on strings, lists etc
""""
num_char = len(input("what is your name"))
"""
# print("your name has"+ num_char + "characters")
# this will give you an error as you can't concatenate a string and an integer directly
# to fix it you need to convert num_char to a string
# there a function named type that will tell what data type you are working with
"""
print(type(num_char))
"""
# convert num_char to a string
""""
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters")
a = 123
print(type(a))
b = str(a)
print(type(b))
c = float(123)
print(type(c))
"""
# exercise 1
# write  a program that adds the digits in a 2 digit number and prints the sum
"""
two_digit_number = input()
num_1 = int(two_digit_number[0])
num_2 = int(two_digit_number[1])
print(num_1 + num_2)
"""
# the math operators that you have access to in python are 
""""
print(3+5) # addition
print(7-4) # subtraction
print(3*2) # multiplication
print(6/3) # division this will always give a float
print(2**3) # exponent
print(15%7) # modulus (remainder of division)
"""
# pemdas order is followed in python left to right
# p - parentheses()
# e - exponents**
# m - multiplication*
# d - division/
# a - addition+
# s - subtraction-
"""
print(3 * 3 + 3 / 3 - 3)
"""
# change this line to get 3 instead of 7
"""
print(3 * (3 + 3) / 3 - 3)
"""
# exercise 2
# write a program that calculates someones bmi
# bmi formula: weight(kg) / height(m)^2
"""
height = input()
weight = input()
BMI = float(weight)/float(height)**2
print(int(BMI))
"""
# the round function will round a number to the closest integer
# you can specify how many decimal places to round to
"print(round(8 / 3, 2))"
# will give you 2.67 rounded to 2 decimal places
# the // operator performs floor division, always rounding down to the nearest whole number
"print(8 // 3)" # this ia a int
# f{strings} this converts numbers and boolean  data types to strings
"""print(f'your bmi is {BMI}')"""
# e.g of how an f-string works
""""
score = 0
height = 1.0
winning = True
print(f"My height is {height}m. I'm winning: {winning} ,your score is {score}")
"""
# exercise 3
# write a program that calculates the how many weeks left until a person turns 90
"""
age = input()
age_int = int(age)
years_left = 90 - age_int
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left.")
"""
# == is for the answer , well = is for assigning variables
# tip calculator 
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator")
bill = float(input("What was the total bill? "))
num_people = int(input("How many people are splitting the bill?"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15? don't add %"))/100
total_tip = bill * tip_percent
total_bill = bill + total_tip
paying_each = round((total_bill / num_people), 2)
print(f"Each person should pay: ${paying_each}")


