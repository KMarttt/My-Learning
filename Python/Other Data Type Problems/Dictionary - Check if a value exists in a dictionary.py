sample_dict = {'a': 100, 'b': 200, 'c': 300}
values = []
for x in sample_dict:
    # gets the value of the keys in the dict
    values.append(sample_dict.get(x))

if 200 in values:
    print("200 present in a dict")
else:
    print("nawp")


