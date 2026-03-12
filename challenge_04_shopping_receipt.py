item1_name = input("Enter item 1 name: ")
item1_price = float(input("Enter item 1 price: "))

item2_name = input("Enter item 2 name: ")
item2_price = float(input("Enter item 2 price: "))

item3_name = input("Enter item 3 name: ")
item3_price = float(input("Enter item 3 price: "))

total = item1_price + item2_price + item3_price

print("\n" + "-"*25)

print(f"{item1_name:<15} ${item1_price:>8.2f}")
print(f"{item2_name:<15} ${item2_price:>8.2f}")
print(f"{item3_name:<15} ${item3_price:>8.2f}")
print("-"*25)
print(f"{'TOTAL':<15} ${total:>8.2f}")
