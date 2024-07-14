def safe_divide(numerator, denominator):
    try:
        try:
            num = float(numerator)
            den = float(denominator)
            return print("The result of the division is "+ str(num/den))
        except:
            print("Error: Please enter numeric values only.")
    except:
        print("Error: Cannot divide by zero.")