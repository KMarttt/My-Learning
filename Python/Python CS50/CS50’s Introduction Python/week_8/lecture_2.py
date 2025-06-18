import random

"""Instance Method"""
# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]
#     #     so this is the default values for the class
#     #     so you can use it in various methods
#
#     def sort(self, name):
#         # this will randomly pick house from the self.houses
#         print(name, "is in", random.choice(self.houses))
#
#
# hat = Hat()
# hat.sort("Harry")



"""Class methods"""
# this program does not allow you to instantiate object
# cuz really, there is only one sorting hat
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]
    # this is now a class variable

    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
