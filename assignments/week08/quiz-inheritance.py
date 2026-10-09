""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:
    
    def __init__(self, brand, model,year): 
        self.brand = brand 
        self.model = model 
        self.year = year 

    def get_info(self):
        def brand(self):
            print(f"{self.brand} brands")
        
        def model(self):
            print(f"{self.model} is model vahicle")
        
        def year(self):
            print(f"{self.year} is year of manufacture")

class Car(Vehicle):
    def __init__(self,brand, model,year,number_of_doors):
        super().__init__(brand, model,year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Car info:\nBrand{self.brand}, Model{self.model}, Year: {self.year}, Numbers_of Doors: {self.number_of_doors}"
