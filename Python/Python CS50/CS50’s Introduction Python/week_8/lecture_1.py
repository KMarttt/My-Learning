"""Return tuple"""

# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")
#
# def get_student():
#     name =  input("Name: ")
#     house = input("House: ")
#     return name, house

# whenever you use the return ... , ...
# this actually returns a tuple (immutable) and not two items
# to explicitly say that the code is tuple, you can enclose the following
# with parenthesis


"""Return list"""
#  so you can change returned values

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")
#
# def get_student():
#     name =  input("Name: ")
#     house = input("House: ")
#     return [name, house]
# # return square brackets return a list


"""Returning dictionary"""
# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")
#
# def get_student():
#     # student = {}
#     # student["name"] = input("Name: ")
#     # student["house"] = input("House: ")
#     # return student
#
# #     OR
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name":name, "house": house}



"""class"""

# class Student: # defining a class
#     ...
#
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
#
# def get_student():
#     student = Student()  # this is creating of objects
#     student.name = input("Name: ") # storing of data in the class
#     student.house = input("House: ") # these names & house are class instance variable
# #     this is attribute creation of class
#     return student
#
# # ... is like a pass - a temporary placeholder



"""__init__"""
#
# class Student:
#     def __init__(self, name, house=None):
#         # parameter self is the current object
#         # this take in name & house
#
#         # you can add default value to make some initialization component optional
#
#         # this the value checking of classes:
#         if not name: # means name == ""
#             raise ValueError("Missing Name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
#             raise ValueError("Invalid House")
#
#
#         self.name = name # this is an instance variable
#         self.house = house
#
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # try:
#     return Student(name, house)
#     # except ValueError:
#     #     ...
#
#
#     # this is a constructor call
#     # we are passing argument into the Class
#     # and then you can customize those contents if you want
#     # is going to use Student class as a mold
#
#     # analogy: same house in the neighborhood but different interior stuff
#     # like the class, every object is the same while having different data/values




"""__str__"""
# class Student:
#     def __init__(self, name, house=None):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#
# def main():
#     student = get_student()
#     print(student)
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # try:
#     return Student(name, house)
#     # except ValueError:
#     #     ...


"""own method"""
# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#     def charm(self):
#         if self.patronus == "Stag":
#             return "*Stag emoji"
#         elif self.patronus == "Otter":
#             return "*Otter emoji"
#         elif self.patronus == "Jack Russel Terrier":
#             return "*Jack Russel Terrier emoji"
#         else:
#             return "NO patronus in the record, NERD"
#
#
#
# def main():
#     student = get_student()
#     print("Expecto Patronum")
#     print(student.charm())
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     # try:
#     return Student(name, house, patronus)
#     # except ValueError:
#     #     ...



"""Properties"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    #         if assigning, this will call setter.house
    #         if accesing the house value, this will call the @property of def house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    # Getter - gets attributes
    @property
    # - used to access the _house which is the implicit value of house
    def house(self):
        return self._house

    # Setter - set values
    @house.setter
    # used to validate house as well as implicitly equate it to _house
    # used for ASSIGNING
    # hence, if self.house is called the house method (@propety) would be called and use data of _house
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError ("Invalid House")
        self._house = house
#         _house is a naming convention to avoid having the same
#         instance variable and method

def main():
    student = get_student()
    # student.house = "GMA"
    # this won't work based on the validation placed in the class
    # if you were to try to change something, it will first have to be validated by the setter
    # instead of changing its value right away

    # tho, if you were to do student._house = "GMA"
    # the validation won't work since self._house is not part of the validation
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # try:
    return Student(name, house)
    # except ValueError:
    #     ...

# in this code, were trying to prevent the programmer to modify the data in the class
# and to do this:
# you are required to go through functions in order to set some attributes
# those function are the getter and setter
if __name__ == "__main__":
    main()