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

        # Attempt division
        result = num / den
        return f"The result of dividing {num} by {den} is {result:.2f}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Both numerator and denominator must be numeric values."
    except ZeroDivisionError:
        # Handle division by zero (must match test exactly!)
        return "Error: Cannot divide by zero."
