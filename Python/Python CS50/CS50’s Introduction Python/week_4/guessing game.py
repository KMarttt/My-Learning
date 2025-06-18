from random import  randint

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue

    if n < 0:
        continue
    else:
        break


level = randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue


    if guess < 0:
        continue
    elif guess < level:
        print("Too small!")
    elif guess > level:
        print("Too large!")
    elif guess == level:
        print("Just right!")
        break
    else:
        continue



