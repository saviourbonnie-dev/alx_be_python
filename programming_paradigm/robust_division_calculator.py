# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero and invalid inputs.
    Returns either the result or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result:.1f}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

