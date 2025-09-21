"""
Ask user to imput a number
use the inputed number to generate a time table

define two for loops:
loop one prints the number of iteration
loop two prints the multiplication table
"""

number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
	print(f"{number} * {i} = {number * i}")

