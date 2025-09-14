"""
# Personal Finance Calculator

#User Input for Financial Details:
monthly_income = float(input("Enter your monthly income: "))

#Calculate Monthly Savings:
total_monthly_expsense = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expsense
print("Your monthly savings are", sep'$', monthly_savings)
#Project Annual Savings:
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Projected Savings after one year, with interest, is:", sep'$', projected_savings)
"""
# Personal Finance Calculator

monthly_income = float(input("Enter your monthly income: "))
total_monthly_expense = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expense
print(f"Your monthly savings are: ${monthly_savings:.2f}")

projected_savings = monthly_savings * 12 * 1.05
print(f"Projected Savings after one year, with interest, is: ${projected_savings:.2f}")
