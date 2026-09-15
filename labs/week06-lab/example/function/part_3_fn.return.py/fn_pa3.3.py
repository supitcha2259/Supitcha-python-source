# Example 3: Using returned values in expressions
def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def square(n):
    """Returns the square of a number"""
    return n * n

print("Using return values in expressions:")
result = multiply(4, 5) + square(3)
print(f"multiply(4, 5) + square(3) = {multiply(4, 5)} + {square(3)} = {result}")
print()

"""Output: Using return values in expressions:
multiply(4, 5) + square(3) = 20 + 9 = 29"""