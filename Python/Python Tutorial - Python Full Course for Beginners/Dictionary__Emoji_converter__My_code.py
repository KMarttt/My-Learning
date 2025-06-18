




text = input("> ")

emoji = {
    ":)": "😊",
    ":(": "🙁",
    ">:(": "😡",
    ":D": "😀",
    ":P": "😛",
    ";)": "😉",
    ":/": "😕",
    ":O": "😮",
    "<3": "❤️"
}

word_list = []
word_stored = ""
for character in text:
    if character != " ":
        word_stored += character
    elif character == " ":
        # the space marks as the boundary for the word then it saves it in the list
        if word_stored != " ":
            # code above checks if the word_stored is not empty in order to avoid saving nothing in the list
            word_list.append(word_stored)
            word_stored = ""
if word_stored != "":
    # this is for the end word where a user might not have inserted a space
    word_list.append(word_stored)
    word_stored = ""




# for word in word_list:
#         print(emoji[word], end=" ")

keys = emoji.keys() # this creates a list of keys in the emoji dictionary

for word in word_list:
    emojication_executed = False
    for key in keys:
        if word == key:
            # Checks whether the word is equals to the keys (which is a word emoji) in the emoji dictionary
            print(emoji[word], end=" ")
            emojication_executed = True
    else:
        if emojication_executed == True:
            continue
        # So if the emojication was executed, it would no longer print out the text version of the emoji
        else:
            print(word, end=" ")
        # If there is no emoji, then only the word will be printed





