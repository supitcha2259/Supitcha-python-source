"""
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD (1 USD = 32 THB)

โดยใช้ชื่อ 
function convert_currency(100,"USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3... USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""

def convert_currency(T,U):
    if U == "USD": #แปลงบาทเป็นดอลลาร์
        T/32.0
        print(f"{T} THB = {T/32.0} USD")
    else: #แปลงดอลลาร์เป็นบาท
        T*32.0
        print(f"{T} USD = {T*32.0} THB")

convert_currency(100,"USD")
convert_currency(100,"THB")