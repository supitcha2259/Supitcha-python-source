# ตัวอย่างที่ 1: คำนวณพื้นที่และปริมตรสี่เหลี่ยม
print("Rectangle Calculator")
print("-" * 20)
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area = length * width = {length} * {width} = {area}")
print(f"Perimeter = 2 * (length + width) = 2 * ({length} + {width}) = {perimeter}")
print()