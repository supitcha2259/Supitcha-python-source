# ===========================
# 4. TRAVERSING STRINGS
# ===========================

print("\n=== TRAVERSING STRINGS ===")
message = "hello"
index = 0

print("Method 1: Using for loop with enumerate")
for i, char in enumerate(message):
    print(f"message[{i}] = {char}")

print("\nMethod 2: Manual indexing")
index = 0
for char in message:
    print(f"message[{index}] = {char}")
    index += 1