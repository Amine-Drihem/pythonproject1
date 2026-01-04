
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "chips": 1.00,
        "fries": 2.50,
        "soda": 3.00}

cart = []
total = 0

print("------menu------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}$")
print("-----------------")

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif food not in menu.keys():
        print("ce n'est pas inclus dans le menu")
    else:
        cart.append(food)

print("-----your order-----")
for food in cart:
   total += menu.get(food)
   print(food, end = " ")
print("")
print(f"the total is {total:.2f}$")