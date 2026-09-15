# + - * / // % ** ในไพทอน
#1. **
#2. * / // %
#3. + -
print("=" * 50)
print("DEMO 3: Operator Precedence")
print("=" * 50)

# ตัวอย่างลำดับการคำนวณ
expression1 = "2 + 3 * 4"
result1 = 2 + 3 * 4
print(f"{expression1} = {result1}")
print("Explanation: * has higher precedence than +")
print("So: 2 + (3 * 4) = 2 + 12 = 14")
print()

expression2 = "(2 + 3) * 4"
result2 = (2 + 3) * 4
print(f"{expression2} = {result2}")
print("Explanation: Parentheses have highest precedence")
print("So: (2 + 3) * 4 = 5 * 4 = 20")
print()

expression3 = "2 ** 3 * 4"
result3 = 2 ** 3 * 4
print(f"{expression3} = {result3}")
print("Explanation: ** has higher precedence than *")
print("So: (2 ** 3) * 4 = 8 * 4 = 32")
print()

expression4 = "10 / 2 * 3"
result4 = 10 / 2 * 3
print(f"{expression4} = {result4}")
print("Explanation: / and * have same precedence, evaluate left to right")
print("So: (10 / 2) * 3 = 5.0 * 3 = 15.0")
print()