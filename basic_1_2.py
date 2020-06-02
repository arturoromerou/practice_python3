import calendar

"""12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. """

# SOLUTION EXERCISE 12:
y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
print("")
print(calendar.month(y, m))
