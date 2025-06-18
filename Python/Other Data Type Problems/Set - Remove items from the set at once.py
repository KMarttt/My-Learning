# Write a Python program to remove items 10, 20, 30 from the following set at once.

set1 = {10, 20, 30, 40, 50}
itemToBeRemoved = {10, 20, 30}
set1.difference_update(itemToBeRemoved)
print(set1)