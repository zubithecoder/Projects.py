# Making a Concession Stand Program Using Only Python

menu = {
    "popcorn": 6.00,
    "soda": 3.00,
    "chips": 1.00,
    "pretzels": 3.50,
    "nachos": 4.50,
    "fries": 2.50,
    "lemonade": 4.25,
    "pizza": 3.00
}

cart = []   # list to store selected items
total = 0   # variable to store total price

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")  
    # {key:10} → gives space of 10 chars for item name
    # {value:.2f} → shows 2 decimal places for price
print("---------------------------")

while True:
    food = input("Enter an item to add to your cart (q to quit): ").lower()

    if food == "q":
        break  # stop taking orders
    elif food in menu:
        cart.append(food)  # add valid item to cart
    else:
        print("Item not found! Please try again.")  # wrong input

print("--------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)  # add price to total
    print(food, end=" ")  # show ordered items
print()

print(f"Total is: ${total:.2f}")  # show final total
