# message = input("> ")
# words = message.split(' ')
            # this code finds ' ' (space) then splits the text
            # its a boundary to separate the sentence into multiple words

# emojis = {
#     ":)": "😊",
#     ":(": "🙁",
#     ">:(": "😡",
#     ":D": "😀",
#     ":P": "😛",
#     ";)": "😉",
#     ":/": "😕",
#     ":O": "😮",
#     "<3": "❤️"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
                # we try to find the word in the keys of the dictionary
                # if its not there, then it will have a default value of its word

                # the output acts as a holder of words
# print(output)

"""Converting it to function"""
def emojication(message):
    words = message.split(' ')

    emojis = {
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
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
text_w_emoji = emojication(message)
print(text_w_emoji)





