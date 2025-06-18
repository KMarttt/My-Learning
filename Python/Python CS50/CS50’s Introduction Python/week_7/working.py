# will convert meridiem time to military time

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^([0-9]|1[0-2]):?([0-9]|[0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-9]|[0-5][0-9])? (AM|PM)$", s)


    # this code will check if the string matches the pattern
    if matches:
        # if it matches, then it will rename the following for readability
        hour1, min1, meridiem1, hour2, min2, meridiem2 = matches.group(1),matches.group(2), matches.group(3), matches.group(4),matches.group(5),matches.group(6)
    else:
        raise ValueError()

    # this code will check AM and PM of hours
    # if AM then it will check if its one digit or 2
    # if one digit = add "0" prefix, else do nothing
    # if pm then add 12
    if meridiem1 == "AM":
        if len(hour1) == 1:
            hour1 = "0" + hour1
    elif meridiem1 == "PM":
        hour1 = int(hour1)
        hour1+=12

    if meridiem2 == "AM":
        if len(hour2) == 1:
            hour2 = "0"+hour2
    elif meridiem2 == "PM":
        hour2 = int(hour2)
        hour2 += 12

    # if the uses didn't input minutes to the time, then this code will set minutes to "00"
    if min1 == None:
        min1 = "00"
    if min2 == None:
        min2 = "00"

    return f"{hour1}:{min1} {meridiem1} to {hour2}:{min2} {meridiem2}"


if __name__ == "__main__":
    main()