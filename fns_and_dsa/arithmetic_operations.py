def perform_operation(num1, num2, operation):
    if operation == "add":
        resp = num1 + num2
        return resp
    elif operation == "subtract":
        resp = num1 - num2
        return resp
    elif operation == "multiply":
        resp = num1 * num2
        return resp
    elif operation == "divide":
        if num2 == 0:
            return "Enter the valid number"
        else:
            resp = num1 / num2
            return resp
    
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Enter the operation (add, subtract, multiply, divide):")

print(f"Result: {perform_operation(num1, num2, operation)}")