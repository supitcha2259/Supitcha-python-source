"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self): #พื้นที่
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self): #ความยาวรอบรูป
        return 2 * (self.length + self.width)

#ตัวอย่างการใช้งาน
rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

"""
ขอให้เขียนคลาส Circle ที่ทำงานคล้ายกับ Rectangle พร้อมตัวอย่างการใช้งาน
"""
class Circle:
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius


    # Method to get the area
    def get_area(self): #พื้นที่
        return self.radius * self.pi **2

    # Method to get the perimeter
    def get_perimeter(self): #ความยาวรอบรูป
        return 2 * (self.pi*self.radius)

rect = Circle(5)
print(rect.get_area())      
print(rect.get_perimeter())