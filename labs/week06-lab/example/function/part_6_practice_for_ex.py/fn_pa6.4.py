# Example 4: Simple calculator functions
def add(a, b):
    """Addition"""
    return a + b

def subtract(a, b):
    """Subtraction"""
    return a - b

def multiply(a, b):
    """Multiplication"""
    return a * b

def divide(a, b):
    """Division with zero check"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Calculator Functions:")
x, y = 12, 4
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} × {y} = {multiply(x, y)}")
print(f"{x} ÷ {y} = {divide(x, y)}")
print(f"{x} ÷ 0 = {divide(x, 0)}")
print()