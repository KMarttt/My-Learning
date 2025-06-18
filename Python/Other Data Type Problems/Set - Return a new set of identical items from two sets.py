"""Identical"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()

for x in set1:
    if x in set2:
        set3.add(x)
print(set3)
print()





