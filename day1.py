# day 1 is printing to the console in python today I will just be print things to the terminal
# the "hello world"is a string and print is a command to out put it to the terminal
# a string is just normal text 
""""
print("hello world!")
"""
# excise 1 
# answer 1
"""
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
"""
# \n is a special character that creates a new line
"""
print("Hello world \n Hello world")
"""
# + will join strings with out " " unless you add a space between the strings
"""
print("Hello" + " " + "world")
"""
# excise 2
# answer 2
""""
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
"""

# the input function allows the user to input text from the keyboard
"""name = input("What is your name? ")"""
# you can use the data colleted from the input function
# in your code like this 
"""
print("Hello " + name)
"""
# exercise 3 
# answer 3
""""
num1 = int(input())
num2 = int(input())
print(num1 * num2)
"""
# exercise 4 is to calculate how letter are in the username by creating a function
#answer 4
"""
name = input("What is your username? ")
length = len(name)
print (length)
"""
# a variable is created to store user input
"""
name = input("What is your name?")
"""
# exercise 5
# answer 5
"""
a = input
b = input

c = a
a = b
b = c

print(a, b)
"""
# you can name variables anything you want, as long as they follow the rules for naming variables in python

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")

#2. Ask the user for the city that they grew up in.
city_name = input("What city did you grow up in? ")

#3. Ask the user for the name of a pet.
pet_name = input("What is your pet's name? ")

#4. Combine the name of their city and pet and show them their band name.
band = city_name+ " " + pet_name

#5. Make sure the input cursor shows on a new line:
print("your band name could be:\n", band)
