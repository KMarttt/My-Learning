input = input("Input: ")
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
text=""

for char in input:
    if char in vowels:
        continue
    else:
        text += char
print(text)