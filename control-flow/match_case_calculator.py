"""
1. prompt user to enter two numbers
2. select an operation : (+,-,*,/)
3. use match_case statement tto perform tassk
"""

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
	case "+":
		print(f"The result is {number_1 + number_2}")
	case "-":
		print(f"The result is {number_1 - number_2}")
	case "*":
		print(f"The result is {number_1 * number_2}")
	case "/":
		if  number_2 == 0:
				print("Cannot divide by zero.")
		else:
			print(f"The result is {number_1 / number_2}")
	case _:
		print("Enter a valid operator" )
