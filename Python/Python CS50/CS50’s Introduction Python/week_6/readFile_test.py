"""Long Version"""
# with open("names.txt", "r") as file:
#     lines = file.readlines()
# # lesson learned it should be .readlines() with s to save the lines
# # .readline() with no s will only read a line, and store it in the variable per character
# #
#
# for line in lines:
#     """print("Hello", line, end="")"""
#     # new line is coming from the text line, so no need to
#     # add yet another new line in printing to avoid double line
#     """you could also do this"""
#     print("hello", line.rstrip())
#     # .rstip can be used to strip off anything that is in the end of the line
#     # and let print do its work

"""Shorter Version"""
# with open("names.txt", "r") as file:
#     for lines in file:
#         print("Hello,", lines.rstrip())
#     # based on my understanding, there is no longer a need to read all of the lines
#     # then save it to a list to iterate
#     # instead you can just iterate every line in the file


"""To sort the lines (alphabetically)"""
# names = []
#
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):
#     print("Hello,", name)

"""Shorter sorter version"""

with open("names.txt", "r") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())