""""""
"""SET"""
""""""

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]
#
# """ this makes it, so you can get the unique houses from the list above """
#
# # houses = []
# # for student in students:
# #     if student["house"] not in houses:
# #         houses.append(student["house"])
# #
# # for house in sorted(houses):
# #     print(house)
#
# """ you can achieve the result of the above code using set """
#
# houses1 = set()
#
# for student in students:
#     houses1.add(student["house"])
#
# for house in sorted(houses1):
#     print(house)



""""""
"""global"""
""""""

# balance = 0
#
# def main():
#
#     print ("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)
#
# def deposit(n):
#     global balance
#     balance += n
#
# def withdraw(n):
#     global balance
#     balance -= n
#
# if __name__ == "__main__":
#     main()

""""""
"""Using OOP for global function"""
""""""

# class Account:
#     def __init__(self):
#         self._balance = 0
#
#     @property
#     # allows the programmer to control how it can be read
#     def balance(self):
#         return self._balance
#
#     def deposit (self, n):
#         self._balance += n
#
#     def withdraw(self, n):
#         self._balance -= n
#
# def main():
#     account = Account()
#     print("Balance", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance", account.balance)
#
# if __name__ == "__main__":
#     main()



"""Constant"""

# MEOWS = 3
# for _ in range (MEOWS):
#     print("meow")


# class Cat():
#     MEOWS = 3
#3
#     def meow(self):
#         for _ in range (Cat.MEOWS):
#             print("meow")
#
# cat = Cat()
# cat.meow()

""""""
"""Type hints"""
""""""

"""mypy"""

def meow(n: int):
    """
    Meows n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string or n meow, one per line
    :rtype: str
    """
    return "meows\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")