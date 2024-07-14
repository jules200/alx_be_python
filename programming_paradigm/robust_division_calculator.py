def safe_divide(numerator, denominator):
    try:
        try:
            num = float(numerator)
            den = float(denominator)
            return print(num/den)
        except:
            print("Invalid in put")
    except:
        print("Error: Cannot divide by zero.")