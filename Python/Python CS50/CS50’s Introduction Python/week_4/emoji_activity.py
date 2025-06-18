from emoji import emojize

text = input("Input: ")
emojize_text = emojize(text, language='alias')
print(emojize_text)