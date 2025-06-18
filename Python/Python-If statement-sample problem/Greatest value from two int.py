# Take two int values from user and print greatest among them.

a=int(input("Insert number (a): "))
b=int(input("Insert number (b): "))

if a > b:
    print("Number (a)", a, "is greater than", "Number (b)", b)
elif b > a:
    print("Number (b)", + b, "is greater than", "Number (a)", a)
else:
    print("Both are Equal")
