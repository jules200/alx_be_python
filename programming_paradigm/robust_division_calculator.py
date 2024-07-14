def safe_divide(numerator, denominator):
    try:
        
        num = float(numerator)
        den = float(denominator)
        result = "The result of the division is "+ str(num/den)
        return result
        
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero."
        return result
    except ValueError:
        result = "Error: Please enter numeric values only."
        return result
        