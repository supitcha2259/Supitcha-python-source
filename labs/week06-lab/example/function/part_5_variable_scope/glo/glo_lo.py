# Global variables
global_message = "I'm a global variable"
counter = 0

def demonstrate_scope():
    """Demonstrates local vs global scope"""
    # Local variable
    local_message = "I'm a local variable"
    
    # Accessing global variable
    print(f"Inside function - Global: {global_message}") #เรียกใช้โดยตรงได้
    print(f"Inside function - Local: {local_message}")
    
    # Modifying global variable (need global keyword)
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print("Scope demonstration:")
print(f"Before function call - Counter: {counter}")
demonstrate_scope()
print(f"After function call - Counter: {counter}")
print(f"Outside function - Global: {global_message}")
# print(local_message)  # This would cause an error! เพราะมันจำกัดแค่ใน local ที่อยู่ใน def ไม่ใช่ global ที่เรียกใช้ได้ตรงๆ เพราะอยู่นอกฟังก์ชัน
print()