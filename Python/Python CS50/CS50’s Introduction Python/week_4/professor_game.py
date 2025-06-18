import random


def main():
    level = get_level()     # will get level to determine the num of digit
    score = 0
    for problem in range (0, 10):   # will give problem 10 times
        x, y = generate_integer(level)   # generate integers
        answer = x + y

        for _ in range (0, 3):  # will give the same problem 3 times if the user_answer in incorrect
            try:
                user_answer = int(input(f"{x} + {y} = "))
            except (ValueError):    # if input not int
                pass
            """if a problem occur with the ValueError, the code will still run and print EEE,
            meaning incorrect input, thus consuming the tries that the user has"""
            try:
                if user_answer == answer:
                    score += 1  # will add score if the user_answer is correct
                    break   # and break the loop
                elif user_answer != answer:
                    print("EEE")
            except UnboundLocalError:   # since there was an error in the upper code, this error will occur
                print("EEE")
        else:
            print(f"{x} + {y} = {answer}")  # will give the asnwer after 3 incorrect tries


    print(f"Score: {score}")    # after the series of problems, the score will be displayed


def get_level():
    # will only get 1, 2, 3, as input
    while True:
        n = int(input("Level: "))
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            continue


def generate_integer(level):
    # will generate number based on the level -- related to the number of digit of a number
    if level == 1:
        min_digit = 1
        max_digit = 9
    elif level == 2:
        min_digit = 10
        max_digit = 99
    elif level == 3:
        min_digit = 100
        max_digit = 999

    x_integers = random.randrange(min_digit, max_digit)
    y_integers = random.randrange(min_digit, max_digit)

    return x_integers, y_integers


if __name__ == "__main__":
    main()