# Parent class (Base class)
class Animal:
    
    def __init__(self, name, species): #def ใน class = method
        self.name = name #data1
        self.species = species #data2
        self.is_alive = True #data3
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
class Dog(Animal): #มี parent มากกว่า 1 ได้
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed #ส่วนที่เติมเข้าไป
    
    # Method overriding ลูกเขียน Method ชื่อซ้ำแม่
    def make_sound(self): #เขียนพฤติกรรมชื่อซ้ำแม่ แต่สามารถปรับเปลี่ยนอะไรเฉพาะจุดได้
        print(f"{self.name} barks: Woof!")
    
    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self): #ปรับจากคลาสแม่
        print(f"{self.name} meows: Meow!")
    
    def climb_tree(self): #เพิ่ม Method
        print(f"{self.name} is climbing a tree")

# Usage
dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.eat()        # Inherited method
dog.make_sound() # Overridden method
dog.fetch()      # Dog-specific method

cat.make_sound() # Overridden method
cat.climb_tree() # Cat-specific method