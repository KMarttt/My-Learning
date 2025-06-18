import sys

def main():
    fraction = input("Fraction: ")
    percentage, x_int, y_int = convert(fraction)
    print(gauge(percentage, x_int, y_int))

"""Correct code"""
def convert(fraction):
    try:
        x, y =fraction.split("/")
        x = int(x)
        y = int(y)
        percentage = (x/y) * 100
    except (ValueError, ZeroDivisionError):
        sys.exit("Wrong Value")
    else:
        return percentage, x, y

"""Correct code"""
def gauge(percentage, x_int, y_int):
    if x_int > y_int:
        sys.exit("Wrong Value")
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


"""Incorrect code"""
# def convert(fraction):
#     try:
#         x, y =fraction.split("/")
#         x = int(x)
#         y = int(y)
#         percentage = (x/y) * 100
#     except (ValueError, ZeroDivisionError):
#         sys.exit("Right Value")
#     else:
#         return percentage, y, x

"""Incorrect code"""
# def gauge(percentage, x_int, y_int):
#     if x_int > y_int:
#         sys.exit("Right Value")
#     elif percentage <= 1:
#         return "EF"
#     elif percentage >= 99:
#         return "FE"
#     else:
#         return f"{int(x_int)}%"

if __name__ == "__main__":
    main()

