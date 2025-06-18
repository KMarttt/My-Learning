#  will modify the link to its shorten form (YouTube link)

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^.+ src=\"https?://www\.youtube\.com/embed(/\w+)", s)
    if matches:
        return "https://youtu.be/" + matches.group(1)
    else:
        return None


# things I learned: remember to add + or ?
...


if __name__ == "__main__":
    main()