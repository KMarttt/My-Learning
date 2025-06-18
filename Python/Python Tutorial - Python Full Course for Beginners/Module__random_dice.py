import random

"""My Code"""

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(f"({num1}, {num2}) ")
print()
"""His Code - extra work"""


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)  # a tuple


dice = Dice()
print(dice.roll())
