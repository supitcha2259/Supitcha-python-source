# Mistake 3: Division by zero
print("Division by zero:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("10 / 0 = Error! Cannot divide by zero")
print()