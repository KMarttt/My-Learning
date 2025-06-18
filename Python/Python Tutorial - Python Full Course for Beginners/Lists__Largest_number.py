        #Write a prigram to find the largest number in a list

# numbers = [1,5,7,2,6,]
# large_num = numbers[0]
# for i in numbers:
#     if large_num < i:
#         large_num = i
# print(large_num)

        #or shortcut
# print(max(numbers))

"""Convert to function to be imported"""

def find_large_num(numbers):
    large_num = numbers[0]
    for i in numbers:
        if large_num < i:
            large_num = i
    return large_num
