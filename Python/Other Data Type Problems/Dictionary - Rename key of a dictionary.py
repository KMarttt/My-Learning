sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}


tempValue = sample_dict.get("city")
del sample_dict["city"]
sample_dict ["location"] = tempValue
print(sample_dict)