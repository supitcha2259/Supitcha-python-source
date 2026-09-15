# Example 3: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temp, scale):
    """Converts temperature between scales"""
    if scale.upper() == "C":
        converted = celsius_to_fahrenheit(temp)
        return f"{temp}°C = {converted:.1f}°F"
    elif scale.upper() == "F":
        converted = fahrenheit_to_celsius(temp)
        return f"{temp}°F = {converted:.1f}°C"
    else:
        return "Invalid scale. Use 'C' or 'F'"

print("Temperature Converter:")
print(convert_temperature(25, "C"))
print(convert_temperature(77, "F"))
print(convert_temperature(0, "C"))
print(convert_temperature(32, "F"))
print()