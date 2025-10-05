# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero and invalid inputs.
    Returns either the result or an error message.
    """
    try:
        # Convert inputs to floats (handles numeric strings like "5.5" or "10")
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den
        return f"The result of dividing {num} by {den} is {result:.2f}"

    except ValueError:
        # Raised when conversion to float fails
        return "Error: Both numerator and denominator must be numeric values."
    except ZeroDivisionError:
        # Raised when denominator is 0
        return "Error: Division by zero is not allowed."
