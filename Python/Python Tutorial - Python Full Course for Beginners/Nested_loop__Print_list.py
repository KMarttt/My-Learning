numbers = [5, 2, 5, 2, 2]
#
#
# for i in (numbers):
#     print("x" * i)


"""Nested version >:("""

for i in (numbers):
    for j in range (i):
        print("X", end="")
    print()

print()
"""
What he wants
- really confusing instructions"""

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

print()
number_L= [1, 1, 1, 1, 5]

for x_count in number_L:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
