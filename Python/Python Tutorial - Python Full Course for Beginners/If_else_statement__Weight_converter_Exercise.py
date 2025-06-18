weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ").upper()

if unit == "L":
    converted_weight = weight * 0.45
    print(f"You are {converted_weight} kilogram")
elif unit == "K":
    converted_weight = weight / 0.45
    print(f"You are {converted_weight} pounds")
else:
    print("Incorrect input")




# not case sensetive1