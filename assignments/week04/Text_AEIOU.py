#รับชื่อจริง (หรือข้อความ) จากผู้ใช้
#นับจำนวนสระทั้งหมดในข้อความว่ามีกี่ตัว (a,e,i,o,u)
#โดยต้องใช้ loop for เท่านั้น

#ตัวอย่างหน้าจอ
#What is your name?: Boonchoo
#Your text have 4 vowels

name = input("What is your name?\n")
vowel_count = 0
vowel = list("aeiouAeiou")

for chr in name:
    if chr in vowel:
        vowel_count += 1

print(f"name(or text) from user: {name}")
print(f"Your text have {vowel_count} vowels")
