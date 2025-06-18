# Write a program to remove the duplicates in a list

numbers = [1, 2, 2, 6, 5, 4, 6, 6, 11, 5, 7]

for num in numbers:
    repeat_num = numbers.count(num)
    if repeat_num > 1:
        for j in range(repeat_num):
            numbers.remove(num)
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~")
# wrong reading comprehesion, the program is supposed to remove only the duplicates
# and not the number with duplicates... my bad


#editted version to work with its intended function
numbers_2 = [1, 2, 2, 6, 5, 4, 6, 6, 11, 5, 7]

for num_2 in numbers_2:
    repeat_num_2 = numbers_2.count(num_2)
    if repeat_num_2 > 1:
        for j in range(repeat_num_2-1):
            numbers_2.remove(num_2)
print(numbers_2)
"""Explanation for the order of output:
this code will remove the first occurrence of that object 
and after removing the duplicates, that is when it will start to print the list
"""
print("~~~~~~~~~~~~~~~~~~~~~~")


# This is the solution on YT
numbers_3 = [1, 2, 2, 6, 5, 4, 6, 6, 11, 5, 7]
unique = []

for number_3 in numbers_3:
    if number_3 not in unique:
        unique.append(number_3)
print(unique)

"""Explanation for the order of output:
this code will insert the first occurrence of unique number in the list
and the preceding duplicates will be disregarded 
"""





