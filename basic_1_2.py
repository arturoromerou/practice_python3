import calendar
from datetime import date
import math

"""#12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. """

# SOLUTION EXERCISE 12:
y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
print("")
print(calendar.month(y, m))

"""#13. Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

# SOLUTION EXERCISE 13:
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

"""#14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

# SOLUTION EXERCISE 14:
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print("")
print(delta.days, "days")

"""#15. Write a Python program to get the volume of a sphere with radius 6."""
r = int(input("Enter radius to get the volume: "))
v = 4/3 * math.pi * r**3
print("volume: ", v)

"""#16. Write a Python program to get the difference between a given number and 17, if the number is greater 
than 17 return double the absolute difference."""

num = int(input("Enter a number: "))
