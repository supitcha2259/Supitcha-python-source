#ERRORS (bugs)
#3 Types => 1.Syntax Error 2.Runtime Error 3.Logic Error

"""
age = int(input("Insert your age (!!!NUMBER ONLY!!!): "))
print(age)

สมมติว่าใส่จาก twenty แทน 20 จะทำให้ระบบตายและ error"""

#ValueError Exception
try:
    age = int(input("กรอกอายุ: "))
    print(f"ปีหน้าคุณจะอายุ {age+1} ปี")
except ValueError:
    print("กรุณากรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")

#ZeroDivisionException
try:
    numberator = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))

    result = numberator/denominator
    print(f"ผลลัพธ์ = {result}")

except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วย 0 ได้")

#FieleNotFoundException, PermissionException
try:
    filename = input("ชื่อไฟล์: ")

    with open(filename, "r",encoding = "utf-8") as file: #สิทธิในการเข้าถึงไฟล์
        content = file.read

    print("เนื้อหาในไฟล์")
    print(content)

except FileNotFoundError:
    print(f"ไม่พบไฟล์ชื่อ {filename}")

except PermissionError:
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")

"""
raise ใช้สำหรับสั่งให้ Python สร้าง exception ขึ้นเอง เมื่อข้อมูลหรือสถานการณ์ไม่เป็นตามคำสั่ง
แม้ว่าคำสั่งนั้นจะไม่ผิดไวยากรณ์และ Python ยังทำงานต่อได้ตามปกติก็ตาม
"""

try:
    score = float(input("กรอกคะแนน 0-100: "))

    if not 0 <= score <= 100: #ทำได้แค่ python
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100") #เพื่อดึงเข้าเงื่อนไข excpt ValueError, ไม่เข้า except จะเข้า else

except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")

else:
    print(f"บันทึกคะแนน {score} เรียบร้อย")

finally: #ทำอย่างสุดท้ายทุกกรณี
    print("จบการตรวจสอบคะแนน")