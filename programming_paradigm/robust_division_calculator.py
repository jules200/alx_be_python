def safe_divide(numerator, denominator):
    try:
        
        num = float(numerator)
        den = float(denominator)
        result = num/den
        print("The result of the division is "+ str(num/den))
        return None
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
        