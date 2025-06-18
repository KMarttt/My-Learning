"""Writing - csv.writer"""
# import csv
#
# name = input("What is your name? ")
# home = input("Where is your house? ")
#
# with open("manyTypesOfData_Write_Test.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])


# remember to add heading for the column name
#  this is more of a positional parameter

"""Writing - csv.DictWriter"""

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("manyTypesOfData_Write_Test.csv", "a", newline='') as file:
    writer =csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


# csv.DictWriter
#   - writes data in a dictionary form
#   - remember to add heading for the column name in the text file
#   - then, use fieldnames=[] to make it a keyword argument (use the column names)