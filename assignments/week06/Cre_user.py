""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

"""

def create_user_profile(username,age =18,premium = False):
    if premium == True:
        user_type = "Premium User"
    else:
        user_type = "Standard User"
    return f"{username},(age: {age}),{user_type}"

def prin():
    print()
    print("="*40)
    print()

print(create_user_profile("Boonchoo",40))
prin()
print(create_user_profile("Manee"))
prin()
print(create_user_profile("Piti",23, True))
prin()