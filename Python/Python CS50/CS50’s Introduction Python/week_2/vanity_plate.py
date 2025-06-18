def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    req_two_letter_start = check_two_letter_start(s)
    req_max_char = check_max_char(s)
    req_digit = check_digit(s)
    req_no_punctuation = check_no_punctuation(s)

    if req_two_letter_start == False:
        return False
    elif req_max_char == False:
        return False
    elif req_digit == False:
        return False
    elif req_no_punctuation == False:
        return False
    else:
        return  True


def check_two_letter_start(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def check_max_char(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def check_digit(s):
    end_vanity = "1" # default value if no digit
    for char in s:
        char.isdigit()
        if char.isdigit() == True:
            end_vanity = s[s.find(char):len(s)]
            break

    # checks the nature of vanity
    if end_vanity.startswith("0"):
        return False
    elif end_vanity.isdigit() == False:
        return False
    else:
        return True


def check_no_punctuation(s):
    punctuation = ["<",">","'","/" ,":" ,";", "-","_" , ",", " ", ".", "!", "?"]

    for char in s:
        if char in punctuation:
            return False
        else:
            continue
    return True

main()