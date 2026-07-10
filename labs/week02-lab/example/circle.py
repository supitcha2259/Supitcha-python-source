print("1. Circle Calculator:")
print("   - Ask user for radius") #radius = รัศมี
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

# input
Radius = float(input("Your radius: "))
π = 3.14159
print("Chose 1 or 2","1. Area of Circle","2. Circumference of Circle")
Ask = int(input("1 or 2:"))
if Ask != 1 and Ask != 2:
    while(Ask):
        print("Again please: ")
        Ask = int(input("1 or 2:"))
        break

# process
def Area():
    Ask = 1
    Area = π * Radius ** 2
    return Area

def Circumference():
    Ask = 2
    Circumference = 2 * π * Radius
    return Circumference

# output
if Ask == 1:
    Area_res = Area()
    print(f"Area = {Area_res}")

elif Ask == 2:
    Circumference_res = Circumference()
    print(f"Circumference = {Circumference_res}")