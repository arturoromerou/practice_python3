# This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the 
# interpreter. It is always available.
import sys
import datetime
import math
import os

"""PYTHON EXERCISES BASIC I:

#1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. 
Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		    Up above the world so high,   		
		    Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

# SOLUTION EXERCISE 1:
print("""Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. 
Twinkle, twinkle, little star, \n\tHow I wonder what you are""")

"""#2. Write a Python program to get the Python version you are using."""

# SOLUTION EXERCISE 2:
print("\nPython version", sys.version)

"""#3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""

# SOLUTION EXERCISE 3:
current = datetime.datetime.now()
print("\nla fecha y hora: ")
print (current.strftime("%Y-%m-%d %H:%M:%S"))

"""#4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504"""

# SOLUTION EXERCISE 4:
r = float(input("\nEnter the radius: "))
a = (r**2) * math.pi
print(a)

"""#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them."""

# SOLUTION EXERCISE 5:
first = input("\nEnter your first name: ")
last = input("Enter your last name: ")
print(last, first)

"""#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple 
with those numbers.

Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"""
print("")

# SOLUTION EXERCISE 6:
user_list = input("Enter a list: ")
magic_list = user_list.split(",")
magic_tuple = tuple(magic_list)
print("this is a list: ", magic_list)
print("this is a tuple: ", magic_tuple)
print("")

"""#7. Write a Python program to accept a filename from the user and print the extension of that."""

# SOLUTION EXERCISE 7:
file_user = input("Enter the file name and extension: ")
extension = os.path.splitext(file_user)[1]
print(extension)