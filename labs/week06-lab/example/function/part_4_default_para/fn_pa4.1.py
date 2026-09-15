# Example 1: Function with default parameter
def greet_with_title(name, title="Mr./Ms."): #title="Mr./Ms." เป็นการบอกให้ส่งหรือไม่ก็ได้ในนี้(หากส่งตัวอื่น เช่น Mrs. Dr. ก็ทำได้) แต่ส่งได้ไม่เกิน 2 ตัว
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()