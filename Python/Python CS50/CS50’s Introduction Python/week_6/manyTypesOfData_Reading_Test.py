# with open("manyTypesOfData_toBeRead_Test.csv") as file:
#     for lines in file:
#         row = lines.rstrip().split(",")
#         print(f"{row[0]} studies at {row[1]}")

"""You can also do this for more readability"""
# with open("manyTypesOfData_toBeRead_Test.csv") as file:
#     for lines in file:
#         person, school = lines.rstrip().split(",")
#         print(f"{person} studies at {school}")

"""To sort -- GOOD CODE"""
# with open("manyTypesOfData_toBeRead_Test.csv") as file:
#     for lines in sorted(file):
#         person, school = lines.rstrip().split(",")
#         print(f"{person} studies at {school}")


"""using dict"""
# friends = []
# with open("manyTypesOfData_toBeRead_Test.csv") as file:
#     for line in file:
#         name, school = line.rstrip().split(",")
#         # friend = {}
#         # friend["name"] = name
#         # friend["school"] = school
#         # OR
#         friend = {"name": name, "school": school}
#         friends.append(friend)
#     # explanation:
#     """
#     Outcome:
#     friend = [
#         {
#         friend["name"]: name,
#         school["school]: school
#         }
#         ,
#         or
#         {
#         "name": Marti,
#         "school": DLSU
#         }
#     and so on ...
#     ]
#     """
#
# for friend in friends:
#     print(f"My friend, {friend['name']}, is currently studying at {friend['school']}")


"""To sort using dict -- using function"""
# friends = []
#
# with open("manyTypesOfData_toBeRead_Test.csv") as file:
#     for line in file:
#         name, school = line.rstrip().split(",")
#         friend = {"name": name, "school": school}
#         friends.append(friend)
#
# def get_name(friend):
#     return friend["name"]
#     # in this part, the names are not yet arranged
#
#
#
# for friend in sorted(friends, key=get_name):
#     print(f"My friend, {friend['name']}, is studying at {friend['school']}")


# this code sort the order of dict in the list by looking at the key of the dictionary
# sorted function -- iterates all of the friend element with key of "name" in the friends list
# then sort it out before looping the block of code underneath it

# the get name function has no () after it
# since we want the sorted function to call the get name function for us
# passing a reference to the function itself, not the result of calling the function.
#  if you were to put () after the function,
#  then you would immediately pass the result of the function to the key parameter
#  pass the functions around as arguments to other functions without immediately invoking them.

# for every friend in friends list, get key = friend["name"]
# then sort it
# then do the code below with the arrangement of the sorted keys

# you can specify what key to be used in order to sort things

# python allows you to pass functions as arguments into other functions



"""To sort using dict -- using lambda"""
# friends = []
#
# with open("manyTypesOfData_toBeRead_Test.csv") as file:
#     for line in file:
#         name, school = line.rstrip().split(",")
#         friend = {"name": name, "school": school}
#         friends.append(friend)
#
# for friend in sorted(friends, key=lambda friend: friend["name"]):
#     print(f"My friend, {friend['name']}, is studying at {friend['school']}")



#  lambda is used if you only want to use a function in one place

# syntax explanation: key=lambda friend: friend["name"]
#  lambda - the function
# friend = name of the parameter
#  -- parameter name is reasonable because this will call all the friend in the friend list
#  friend["name"] - we want this function to return the value of the key("name") on all of the dict



"""To sort data with (,) 
    -- will use csv library
    -- csv.reader
"""
# import csv
#
# friends = []
#
# with open("manyTypesOfData_2_toBeRead_Test.csv") as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     friends.append({"name": row[0]}, {"school": row[1]})
#     # OR use unpacking
#     for name, school in reader:
#         friends.append({"name": name, "school": school})
#
# for friend in sorted(friends, key = lambda friend: friend["name"]):
#     print(f"{friend['name']} is currently studying at {friend['school']}")



#  reader = csv.reader(file)
#       - were passing file as input
#       - you still need to put "" on data with (,)


"""To sort data with (,) 
    -- will use csv library
    -- csv.DictReader
"""
import csv

friends = []

with open("manyTypesOfData_2_toBeRead_Dict_Test.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # friends.append({"name": row["name"], "school": row["school"]})
#       we use row["name"] since this is now a dictionary
#       OR use this since the file is already formatted in a dicitonary format so no need to name it
        friends.append(row)



for friend in sorted(friends, key = lambda friend: friend["name"]):
    print(f"{friend['name']} is currently studying at {friend['school']}")



# DictReader
#  - this way it will read each line as dictionary of columns, instead of list of columns
#  - a reader returns list
#  - while a dict reader returns dictionaries one at a time
#  - remember at the top of the csv files, there should be a column name
#  - the output might be the same, but now the code is more robust for changes
#           - adding changes to the csv file won't break the code (e.g. adding more column)
#           - if the columns were to have a diff. position, the code will still work since the column is named
#                   - making it a keyword argument
#