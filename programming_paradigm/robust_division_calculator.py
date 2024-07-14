def safe_divide(numerator, denominator):
    try:
        
        num = float(numerator)
        den = float(denominator)
        return print("The result of the division is "+ str(num/den))
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")