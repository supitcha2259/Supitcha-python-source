"""
-เขียนโปรแกรมตรวจสอบความแข็งแรงของ password
-นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลขอย่างน้อย 1 ตัว, มีตัวอักษร

ตัวอย่าง: 
Insert your password: Boonchoo
Your password is not strong!

Insert your password: Test@123
Your password is strong
"""

#password = input("Insert your password: ")

password = 'Tealr@io8'
lenght = len(password)
print("@" in password)  

has_number = any(char.isdigit() for char in password)
has_letter = any(char.isalpha() for char in password)

if len(password) > 8 and "@" in password and has_number and has_letter:
    print("Your password is strong.")
else:
    print("Your password is not strong!")