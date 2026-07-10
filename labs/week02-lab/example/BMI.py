print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
Weight = float(input("Weight: "))
Height = float(input("Height"))

#process
BMI = Weight / (Height ** 2)

#output
print("BMI =",BMI)