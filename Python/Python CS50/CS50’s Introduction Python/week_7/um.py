# will find all "um" in a string, "um" only thought non-word character are allowed near the um

import re

def main():
    print(count(input("Text: ")))


def count(s):
    # umm = re.findall(r"(um+)", s, re.IGNORECASE)
    umm = re.findall(r"(\bum+\b)", s, re.IGNORECASE)

    print(umm)
    return len(umm)


if __name__ == "__main__":
    main()