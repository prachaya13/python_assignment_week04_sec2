x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

import calculator
print(f"X+Y = {calculator.add(x, y)}")
print(f"X-Y = {calculator.subtract(x, y)}")
print(f"X*Y = {calculator.multiply(x, y)}")
print(f"X/Y = {calculator.divide(x, y)}")
