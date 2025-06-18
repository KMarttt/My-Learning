"""Exercise 1: Print First 10 natural numbers using while loop"""
# i= 1
# while i <11:
#     print(i)
#     i+=1

"""Exercise 2: Print the following pattern"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

"""Exercise 3: Calculate the sum of all numbers from 1 to a given number"""
# num = int(input("Enter number "))
# sum=0
# for i in range (1,num+1):
#     sum = sum+i
# print(sum)

"""Exercise 4: Write a program to print multiplication table of a given number"""

# num = 2
#
# for i in range(1,11):
#     product = 2 * i
#     print(product)

"""Exercise 5: Display numbers from a list using loop"""
# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in (numbers):
#     if i > 500:
#         break
#     if i > 150:
#         continue
#     if i % 5 == 0:
#         print(i)

"""Exercise 6: Count the total number of digits in a number"""
###:( :(
# num = 75869

"""Exercise 7: Print the following pattern"""

# num = 5
# for i in range (5):
#     for j in range (5-i, 0, -1):
#         print(j, end=" ")
#     print()


"""Exercise 8: Print list in reverse order using a loop"""
# list1=[10, 20, 30, 40, 50]
# list=reversed(list1)
# for i in (list):
#     print(i)

"""Exercise 8: Print list in reverse order using a loop"""

# for i in range (-10, -0, 1):
#     print(i)

"Exercise 10: Use else block to display a message “Done” after successful execution of for loop"

# for i in range(5):
#     print(i)
# else:
#     print("Done!")

"Exercise 11: Write a program to display all prime numbers within a range"
###:( :(

"Exercise 12: Display Fibonacci series up to 10 terms"
sum_a = 1
for i in range (10):
    sum_a = sum_a + i
    print(sum_a, end=" ")
