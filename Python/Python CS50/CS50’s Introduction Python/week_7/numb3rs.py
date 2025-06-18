# this code will check the IP address, if it follows the rule 0-255.0-255.0-255.0-255

import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):

     # if re.search(r"^[0-9]+[0-9]?[0-5]?\.[0-9]+[0-9]?[0-5]?\.[0-9]+[0-9]?[0-5]?.[0-9]+[0-9]?[0-5]?", ip):
     # if re.search(r"^([0-225]\.){3}([0-225]\.)", ip):

    # # this works
    # matches = re.split("\.", ip)

    # matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip)
    # i = 1
    # for x in (1,4):
    #     num = matches.group(x)
    #     num = int(num)
    #     if num <=255:
    #         continue
    #     else:
    #         return False
    # else:
    #     return True

     # OR

     matches = re.search(r"^(([0-9]{1,2}|1[0-9]{1,2}|2[0-4][0-9]|2[0-5]{1,2})\.){3}([0-9]{1,2}|1[0-9]{1,2}|2[0-4][0-9]|2[0-5]{1,2})$", ip)
     # pattern : (0-9|10-199|200-249|250-255). - do this 3 times, then one time without the dot
     if matches:
         return True
     else:
         return False


if __name__ == "__main__":
    main()