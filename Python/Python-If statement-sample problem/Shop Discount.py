#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

unit=int(input("Number of Unit(s) Purchased: "))

if unit > 10:
    print("Total Cost (10% Discount):", (unit*100)-((unit*100)*.10))
else:
    print("Total Cost:", unit*100)