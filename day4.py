# list and tuples are similar to lists but they are immutable
# tuples are used to store data that shouldn't be changed
# random numbers are generated using the random module
import random
# this is how to import a module here we are importing the random module

'''random_number = random.randint(1, 10)
print(random_number)'''
# this will give us a random number between 1 and 10
# modules give us access to different functions that are built into python
# and modules are used to organize our code
# this is how to use a function from a module
# modules make it easier to reuse code and work in a team
'''random_float = random.random()
print(random_float)

print(random_float * 5)

love = random.randint(1,100)
print( f"your love score is {love}")'''

# exercise 1
'''import random
coin_num = random.randint(0,1)
if coin_num == 1:
    print("Heads")
else:
    print("Tails")'''
# this is a coin flip game 
# the list is a data structure that stores multiple values in a single variable
# lists are used to store multiple values in a single variable
# lists are mutable meaning they can be changed
# you can store different data types in a single list
"""
USA_states = ["California", "Texas", "New York", "Florida", "Illinois"]
print(USA_states)"""
# this will print the list
# list have an order 
# you can access the values in a list by using the index
# The list data type has some more methods. Here are all of the methods of list objects:
"""
list.append(x)
"""
#   Add an item to the end of the list. Equivalent to a[len(a):] = [x].
"""
list.extend(iterable)"""

#   Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
"""
list.insert(i, x)"""

#    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
"""
list.remove(x)"""

#   Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
"""
list.pop([i])"""

#   Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.
"""
list.clear()"""

#   Remove all items from the list. Equivalent to del a[:].

"""
list.index(x[, start[, end]])"""

#    Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

#    The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
"""
list.count(x)"""

#    Return the number of times x appears in the list.
"""
list.sort(*, key=None, reverse=False)"""

#    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
"""
list.reverse()"""

#   Reverse the elements of the list in place.

"""list.copy()
"""
# Return a shallow copy of the list. Equivalent to a[:].

'''
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)
print(len(states_of_america))'''

'''
states_of_america[1] = "pencilvania"'''
# this will change the value of the second item in the list
# to  add to a list you can use the append method
'''states_of_america.append("New Mexico")'''

# exercise 2
# my solution
"""
names_string = input("enter a list of names separated by a comma and a space")
names = names_string.split(", ")
paying = random.choice(names)
print(f"{paying} is going to buy the meal today!"
"""
# Another solution
'''
names_string = input("enter a list of names separated by a comma and a space")
names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])'''

# When working with list you can in counter  the IndexError
# you can have a list with in another list these are called nested lists

# exercise 3
"""
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position_A = position[0]
position_B = int(position[1])
letters = ["A","B","C"]
letter_index = letters.index(position_A)
map[position_B-1][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

"""


# project
print("Welcome to the Rock, Paper, Scissors game!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("please use the numbers 1, 2, or 3 to choose rock, paper, or scissors")

input_choice = int(input("What do you choose? Type rock(1), paper(2), or scissors(3): "))

computer_choice = random.randint(1,3)

if input_choice == 1 :
    print(rock)
elif input_choice == 2 :
    print(paper)
elif input_choice == 3 :
    print(scissors)

print("Computer chose:")
if computer_choice == 1 :
    print(rock)
elif computer_choice == 2 :
    print(paper)
elif computer_choice == 3 :
    print(scissors)

if input_choice == computer_choice :
    print("Draw!")
elif input_choice == 1 and computer_choice == 2 :
    print("You lose!")
elif input_choice == 1 and computer_choice == 3 :
    print("You win!")
elif input_choice == 2 and computer_choice == 1 :
    print("You win!")
elif input_choice == 2 and computer_choice == 3 :
    print("You lose!")
elif input_choice == 3 and computer_choice == 1 :
    print("You lose!")
elif input_choice == 3 and computer_choice == 2 :
    print("You win!")


