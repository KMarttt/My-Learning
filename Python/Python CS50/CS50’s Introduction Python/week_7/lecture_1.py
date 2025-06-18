# email = input("What's your email? ").strip()
#
# if "@" in email and "." in email:
#     # if "@" and "." in the email text
#     print("Valid")
# else:
#     print("Invalid")



# email = input("What's your email? ").strip()
#
# username, domain = email.split("@")
#
# if username and ("." in domain):
#     # will check the existence of the username
#     # if the username has at least one character, that would be considered True
#
#     # "." in domain is a separate condition
#     print("Valid")
# else:
#     print("Invalid")



# email = input("What's your email? ").strip()
#
# username, domain = email.split("@")
#
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")



import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org|ph)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# you can add more (.) to add more character to the pattern
# (.*) means any number with zero or more repetition

#  (.) has a meaning in the pattern so you need to use \.
#  to avoid misinterpretation you can insert r at the beginning of the pattern
#  this makes it so Python won't interpret backslashes in the usual way
# r = raw string
# placing r is a good habit if you accidentally introduce another backslash

# [^@] means any character except (@) are accepted



# the pattern will be read from left to right