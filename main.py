x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

import lambda_calculator
print(f"X+Y = {lambda_calculator.add(x, y)}")
print(f"X-Y = {lambda_calculator.subtract(x, y)}")
print(f"X*Y = {lambda_calculator.multiply(x, y)}")
print(f"X/Y = {lambda_calculator.divide(x, y)}")
