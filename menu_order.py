#Menu items
menu_items = ["burgers", "fries", "hot dogs"]
print("Menu: \n")
print("1. Burger \n")
print("2. Fries \n")
print("3. Hot dogs \n")

prices = [5, 3, 4]
drink = 2
total_cost = 0
#Coustmer choice
choice = int(input("Pick a menu item using the number 1-3: "))

if choice == 1:
    total_cost += prices[0]
    print("You ordered a", menu_items[0])
    print("Your total is $ ", prices[0])

elif choice == 2:
    total_cost += prices[1]
    print("You ordered a", menu_items[1])
    print("Your total is $ ", prices[1])

elif choice == 3:
    total_cost += prices[2]
    print("You ordered a", menu_items[2])
    print("Your total is $ ", prices[2])
else:
    print("That item is not on the menu")


# Do you want to add a drink
additional = input("Do you want a drink Yes or No: ")

if additional.lower() == "yes":
    print("Drink added")
    total_cost += drink
    print("Your total cost $ ", total_cost)
else:
    print("No drink added")
    print("Your total cost $ ", total_cost)