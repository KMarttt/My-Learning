set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
set3.add(set1.difference_update(set2))
print(set3)