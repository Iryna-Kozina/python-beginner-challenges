name = input("Enter your name: ")
age =int(input("Enter your age: "))
height_metres = float(input("Enter your height in metres: "))
fav_number = int(input("Enter your favourite number: "))

height_cm = int(height_metres * 100)

print("\n" + "="*30)
print(f"{'YOUR PROFILE CARD':^30}")
print("="*30)

print(f"{'Name:':<15} {name}")
print(f"{'Age:':<15} {age} years")
print(f"{'Height:':<15} {height_metres}m ({height_cm}cm)")
print(f"{'Fav Number:':<15} {fav_number}")

print("="*30)
