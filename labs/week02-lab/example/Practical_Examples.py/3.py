# ตัวอย่างที่ 3: คำนวณค่าใช้จ่ายแบ่งเท่าๆ กัน
print("Bill Splitter")
print("-" * 15)
total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))

tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / num_people

print(f"\nBill Breakdown:")
print(f"Original bill: ${total_bill}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")
print()