import math

#Write a program to print absolute value of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1

print("ABSOLUTE VALUE")
num=float(input("Enter a number: "))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
expo=num**2;
absolute_value=math.sqrt(expo)
print("Absolute Value:", absolute_value)

#You may also use if else
#i.e if (+) number, print
# and if (-) number, multiply to negative 1 then print
