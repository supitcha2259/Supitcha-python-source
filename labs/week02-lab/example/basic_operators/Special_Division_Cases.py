dividend = 17
divisor = 5

print(f"Given: {dividend} ÷ {divisor}")
print()

# Regular division (/)
regular_div = dividend / divisor
print(f"Regular division (/):")
print(f"{dividend} / {divisor} = {regular_div}")
print("Result: Float number (decimal)")
print()

# Floor division (//)
floor_div = dividend // divisor
print(f"Floor division (//):")
print(f"{dividend} // {divisor} = {floor_div}")
print("Result: Integer (rounded down)")
print()

# Modulo (%)
modulo = dividend % divisor
print(f"Modulo (%):")
print(f"{dividend} % {divisor} = {modulo}")
print("Result: Remainder after division")
print()

# Verification
print("Verification:")
print(f"{divisor} * {floor_div} + {modulo} = {divisor * floor_div + modulo}")
print(f"Should equal {dividend}")
print()