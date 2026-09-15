# ตัวอย่างที่ 2: แปลงหน่วยอุณหภูมิ
print("Temperature Converter")
print("-" * 25)
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Celsius: {celsius}°C")
print(f"Fahrenheit: (celsius * 9/5) + 32 = ({celsius} * 9/5) + 32 = {fahrenheit}°F")
print(f"Kelvin: celsius + 273.15 = {celsius} + 273.15 = {kelvin}K")
print()