# Example 3: Power function with default exponent
def power(base, exponent=2): #ถ้าไม่ส่งค่า exponent จะอนุมานให้เป็น 2 แต่ถ้าส่งก็จะเป็นค่าตามที่รับ
    """Calculates base raised to exponent (default: square)"""
    return base ** exponent

print("Power function with defaults:")
print(f"power(5) = {power(5)}")  # Square
print(f"power(5, 3) = {power(5, 3)}")  # Cube
print(f"power(2, 4) = {power(2, 4)}")  # Fourth power
print()