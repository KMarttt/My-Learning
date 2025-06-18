"""This code should be a try and except exercise however crtl+z does not work,
hence,EOFError won't appear"""

felipe_menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    food_input = input("Item: ").title()
    if food_input in felipe_menu:
        total += felipe_menu[food_input]
    print(f"Total: {total:.2f}")
    if food_input == "Done":
        break


