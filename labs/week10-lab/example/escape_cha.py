# ===========================
# 10. ESCAPE CHARACTERS
# ===========================

print("\n=== ESCAPE CHARACTERS ===")
print("New line example:")
print("Line 1\nLine 2")

print("Tab example:")
print("Column1\tColumn2\tColumn3")

print("Backslash example:")
print("Path: C:\\Users\\Python")

print("Quote examples:")
print('He said, "What\'s there?"')
print("He said, \"What's there?\"") #ใช้ \ เมื่อเครื่องหมาย '' or "" or """""" ที่ใช้เป็นอันเดียวกัน อยู่ติดกัน
print('''He said, "What's there?"''')

# Raw strings
print("\nRaw string example:")
print("Normal: This is \\x61 \\ngood example")
print(r"Raw: This is \x61 \ngood example")