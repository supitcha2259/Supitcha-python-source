# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age >= 0 and age <= 12:
    print("Child")
elif age > 12 and age <= 19:
    print("Teenager")
elif age > 19 and age <= 59:
    print("Adult")
else:
    print("Senior")
print("=" * 50)

# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    print("=" * 50)
    while True:
        print("\n1. Check Balance") #เงินในบัญชี
        print("2. Withdraw") #ถอนเงิน
        print("3. Deposit") #ฝากเงิน
        print("4. Exit")
        print("=" * 50)
        choice = input("Choose option: ")
        print("=" * 50)
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("Balance:", balance, "Bath")
            print("=" * 50)
        elif choice == "2":
            withdraw = int(input("Enter amount: "))
            if withdraw <= balance:
                balance = balance - withdraw
                print("Withdraw successful")
            else:
                print("Insufficient funds")
            print("=" * 50)
        elif choice == "3":
            deposit = (float(input("Enter amount to deposit: ")))
            new_balance = balance + deposit
            print(f"Deposit success!\nNew balance: {new_balance} Bath")
            print("=" * 50)
        elif choice == "4":
            print("Thank for using!")
            break

else:
    print("Invalid PIN")
print("=" * 50)
