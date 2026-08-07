# Example 3: Mathematical function คำนวณพื้นที่สามเหลี่ยม
def calculate_triangle_area(hight, base):
    """Calculates and displays triangle area"""
    area = 1/2*hight*base
    print(f"Triangle with hight {hight} and base {base}")
    print(f"Area = 1/2 × {hight} × {base} = {area}")
    print()

print("Calculating triangle area:")
calculate_triangle_area(5, 3) # hight = 5 and base = 3
calculate_triangle_area(10, 7) # hight = 10 and base = 7
#ใช้ครบทุกตัว = จบโปรแกรม

"""def calculate_triangle_area(hight, base):
    area = 1/2*hight*base
    return area
area = calculate_triangle_area(hight, base)
print(f"Area = 1/2 × {hight} × {base} = {area}")"""