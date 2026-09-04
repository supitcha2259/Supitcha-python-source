# ===========================
# 7. ITERATING AND COUNTING
# ===========================

# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวนอักขระในข้อความ text

"""ตัวอย่างหน้าจอ
insert your text: Boonchoo Jitnupong
Charecter to find: o
5 letters 'o' found in 'Boonchoo Jitnupong'"""

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("insert your text: ")

for letter in text:
    if letter == 'o': #นับ o จากตัวแปร text
        count += 1
print(f"{count} letters 'o' found in '{text}'")

"""อีกแบบ

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("insert your text: ")
char = input("Character to find: ")

for letter in text:
    if letter == char: #นับ char ตัวที่ต้องการหา
        count += 1
print(f"{count} letters 'o' found in '{text}'")

"""