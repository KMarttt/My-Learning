def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(user_input):

    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        # correct
    # vowels = ["a", "e", "i", "o", "u"]
        # incorrect
    text = ""
    for char in user_input:
        if char in vowels:
            continue
        else:
            text += char
    return text


if __name__ == "__main__":
    main()