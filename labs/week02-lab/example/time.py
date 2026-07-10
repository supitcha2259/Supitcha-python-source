print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

#input
Sec = int(input("Second: "))

#process
Hour = Sec // 3600
Sec_remain = Sec % 3600

minute = Sec_remain // 60
minute_remain = Sec_remain % 60

#output
print("Hours is:",Hour)
print("Minute is:",minute)
print("Second is:",minute_remain)
print(f"Hours = {Hour}, Minute = {minute} and Second = {minute_remain}")
