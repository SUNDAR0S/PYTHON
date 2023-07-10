07.10 3:41 PM
6) Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125}
}

print("Item details before updating:")
print("Grocery =", Grocery)

a= int(input("Display what you want to do?\n1. Add the additional quantity of the cereals\n2. Update the price of the grocery\n3. Add new item\nEnter your choice: "))

if a == 1:
    b= input("Enter the grocery item name: ")
    q= int(input("Enter the quantity of item to be added: "))
    if b in Grocery:
        Grocery[b]["quantity"] += q
        print("Item details after updating:")
        print("Grocery =", Grocery)
    else:
        print("Item not found in the grocery list.")

elif a== 2:
    b = input("Enter the grocery item name: ")
    p = float(input("Enter the new price of the item: "))
    if b in Grocery:
        Grocery[b]["price"] = p
        print("Item details after updating:")
        print("Grocery =", Grocery)
    else:
        print("Item not found in the grocery list.")

elif a == 3:
    b= input("Enter the new grocery item name: ")
    q = int(input("Enter the quantity of the new item: "))
    p = float(input("Enter the price of the new item: "))
    Grocery[b] = {"quantity": q, "price": p}
    print("Item details after updating:")
    print("Grocery =", Grocery)

else:
    print("Invalid choice entered.")
