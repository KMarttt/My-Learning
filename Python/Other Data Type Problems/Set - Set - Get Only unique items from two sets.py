set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.update(set2)

print(set1)
# this works since the set does not allow any duplicates, so it will automatically
# delete the duplicates when combining two sets