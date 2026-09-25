"""

=== 2 types of programming  ===

1) structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง input process output

2) object-oriented programming (OOP) ==> การเขียนโปรแกรมเชิงวัตถุ > java , c#, 
python(เต็มหรือไม่เต็มสตรีมก็ได้)

"""

# design how to slove problem

class ClassName:
    """Class docstring"""

    #1 data to use for sloving problem(attribute) from Constructor method
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value

    #2 What you have to do? , doing = method
    def method_name(self): 
        # Instance method
        return something

# how to create => เอาในคลาสมาใช้
myObj = ClassName(parameters)

#using class
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method_name2()

myObj2 = ClassName(parameters)
print(myObj2.attribute)
print(myObj2.method_name())
myObj2.method_name2()