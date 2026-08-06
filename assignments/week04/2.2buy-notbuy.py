price = []

#input price 6 item
print("Enter price of 6 items:")
for i in range(1,7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

print()
#budget total
budget = int(input("Enter total budget: "))
print()

current_total = 0
bought_items = []

for i in range(len(prices)):
    price = prices[i]

    if current_total + price <= budget:
        status = "buy"
        current_total += price
        bought_items.append(price)
    else:
        status = "cannot buy"

    print(f"Item {i + 1} = {price} -> {status}")
    print(f"Current total = {current_total}")
    print()

remaining_budget = budget - current_total
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaning budget: {remaining_budget}")
