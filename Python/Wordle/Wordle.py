import  random

def get_input(wordle_word):
    # used to acquire the word valid word input
    while True:
        word = input("")
        if len(word) == len(wordle_word):
            return word
        else:
            print("Wordle only accepts", len(wordle_word), "words")

def main():
    print("|~=~=~=~=~=~=~=~| Wordle |~=~=~=~=~=~=~=~|\n\n")
    print(" | W | O | R | D | L | E |")

    wordle_word = "which"

    max_attempt = 5
    attempt = 0

    while attempt < max_attempt:
        print(f"Attempt left:", max_attempt-attempt)
        word_input = get_input(wordle_word)

        # character checker
        word_correction_display = []
        for char in word_input:
            if char in wordle_word:
                if word_input.index(char) == wordle_word.index(char):
                    word_correction_display.append("🟩")
                else:
                    word_correction_display.append("🟨")
            else:
                word_correction_display.append("🟥")

        # to print color indicators
        for color_mark in word_correction_display:
            print(f"| {color_mark} ", end="")
        print("|\n")

        # word validation
        if word_correction_display.count("🟩") == len(word_correction_display):
            print("You Win!🎉")
            break
        attempt+= 1
    else:
        print("You lose! 🤣")
        print("STUPPIIID 😹")

    exit = input("")


# additional feature: add random quotes to taunt the user if they made an incorrect input
# add a random word using csv
# allows them to pick the amount of char for the word in order to increase the difficulty of the game
# try to integrate the code into a class?

if __name__ == "__main__":
    main()