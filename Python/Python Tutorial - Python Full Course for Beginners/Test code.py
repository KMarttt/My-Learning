text = input("Input text with emoji: ")

emoji = {
    ":)": "😊",
    ":(": "🙁",
    ">:(": "😡",
}

word_list = []
word_stored = ""
for character in text:
    if character != " ":
        word_stored += character
    else:
        if word_stored != "":
            word_list.append(word_stored)
            word_stored = ""
if word_stored != "":  # Append the last word if there's any remaining
    word_list.append(word_stored)

print(word_list)
