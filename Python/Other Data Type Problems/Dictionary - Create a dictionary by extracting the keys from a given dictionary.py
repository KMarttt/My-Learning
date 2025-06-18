sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dictionary = {}

# for x in range (0, len(keys)):
#     tempValue = sample_dict.get(keys[x])
#     dictionary [keys[x]] = tempValue

"""improvement"""
for x in keys:
    tempValue = sample_dict.get(x)
    dictionary [x] = tempValue

print(dictionary)