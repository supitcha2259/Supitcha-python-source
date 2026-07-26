print("=" *20,"BMI Calculator","=" *20)
print("=" *60)

Weight = float(input("Weight: "))
Height = float(input("Height: "))

BMI = Weight / (Height ** 2)

print("BMI =",BMI)
print("=" *60)

#Below 18.5: Underweight
#18.5 - 24.9: Normal weight
#25.0 - 29.9: Overweight
#30.0 and above: Obese

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight")
elif BMI > 24.9 and BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")
print("=" *60)