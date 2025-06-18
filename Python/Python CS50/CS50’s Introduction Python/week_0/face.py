def convert(text):
    # converts text to emoji
    if ":)" in text:
        text = text.replace(":)", "🙂")
    if ":(" in text:
        text = text.replace(":(", "🙁")
    return text


text = str(input("Input a text with emoji: "))
converted_text = convert(text)
print(converted_text)

