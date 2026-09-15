# Example 1: Function that returns a value
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()