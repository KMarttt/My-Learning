# will check the validity of the email address

from validator_collection import validators, checkers, errors

if email_address := checkers.is_email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")

