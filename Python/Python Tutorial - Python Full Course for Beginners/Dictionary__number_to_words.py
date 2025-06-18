phone = (input("Phone: "))

numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

for num in (phone):
    print(numbers[num], end=" ")
print()

# """His solution"""
#
# phone_2 = input("Phone: ")
# digit_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
# }
#
output = ""
for ch in phone_2:
     output += digit_mapping.get(ch, "!") + " "
print(output)
#
# """Explanation
# - this is a lazy ass code
# - the dictionary is incomplete
# - if there is no key that represent the number in the dictionary,
# the program will insert ! as a default value
# (ch as the number in the dictionary and "!" as default if there is no ch in the dictionary)
# - MINE'S BETTER!!!!
# """

