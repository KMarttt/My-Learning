#format.py
import re

# name = input("What's you name? ").strip()
#
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
#
# print(f"Hello, {name}")

name = input("What's you name? ").strip()

# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     # last, first = matches.groups()
#
#     # OR
#
#     # last = matches.group(1)
#     # first = matches.group(2)
#     # name = f"{first} {last}"
#
#     # OR
#
#     name = matches.group(2) + " " + matches.group(1)

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)


print(f"Hello, {name}")


# anything surrounded by the parenthesis in the re.search will be captured
#  this will work since there are no (+), (*), or (?) after the parenthesis

# matches.groups()
# will ask all of the group within the re.search
# remember matches.groups(), groups, groupS, with S

# seems lines the numbering index starting from 0 rule does not work with re search
# 1 is the first group parenthesis