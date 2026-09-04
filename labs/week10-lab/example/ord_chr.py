# ===========================
# 13. ORD() AND CHR() FUNCTIONS
# ===========================

print("\n=== ORD() AND CHR() FUNCTIONS ===")
ch = 'R'
print(f"ord('{ch}') = {ord(ch)}")
print(f"chr(82) = {chr(82)}")

# ASCII table example
print("\nASCII values for A-Z:")
for i in range(65, 71):  # A-F
    print(f"chr({i}) = {chr(i)}")