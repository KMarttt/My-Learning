tuple1 = (11, 22)
tuple2 = (99, 88)
tempTup1 = tuple1
tempTup2 = tuple2
tuple1 = tempTup2
tuple2 = tempTup1
print(tuple1)
print(tuple2)

# this could also work
# tuple1, tuple2 = tuple2, tuple1

