# ===========================
# 12. STRING METHODS EXAMPLES
# ===========================

print("\n=== STRING METHODS ===")
text = "welcome to the world of python"

# Case methods
print(f"Original: {text}")
print(f"Upper: {text.upper()}") #ทุกตัวเป็นพิมพ์ใหญ่
print(f"Lower: {text.lower()}") #ทุกตัวเป็นพิมพ์เล็ก
print(f"Title: {text.title()}") #ทุกตัวแรกเป็นพิมพ์ใหญ่
print(f"Capitalize: {text.capitalize()}") 

# Search methods
print(f"Find 'world': {text.find('world')}")
print(f"Count 'o': {text.count('o')}") #นับได้ทั้งอักขระและ str
print(f"Starts with 'welcome': {text.startswith('welcome')}") # start with welcome? (True or False)
print(f"Ends with 'python': {text.endswith('python')}") # Ends with python? (True or False)

# Modification methods
print(f"Replace 'python' with 'java': {text.replace('python', 'java')}") #แทนที่ข้อความ จาก python เป็น java
words = text.split() #['welcome', 'to', 'the', 'world', 'of', 'java']
print(f"Split into words: {words}")
print(f"Join with '-': {'-'.join(words)}") #join เอากลับมารวมกัน

# Validation methods
test_str = "Hello123"
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}") #เป็นตัวเลขทั้งหมดมั้ย , True
print(f"isalpha(): {test_str.isalpha()}") #เป็นตัวอักษรทั้งหมดมั้ย , False
print(f"isdigit(): {test_str.isdigit()}") #เป็นตัวเดียวกัหมดมั้ย
print(f"isupper(): {test_str.isupper()}") #ทุกตัวเป็นพิมพ์ใหญ่มั้ย
print(f"islower(): {test_str.islower()}") #ทุกตัวเป็นพิมพ์เล็กมั้ย