import sys
def main():
    fraction = input("Fraction: ")
    percentage, x_int, y_int = convert(fraction)
    print(gauge(percentage, x_int, y_int))

def convert(fraction):
    try:
        x, y =fraction.split("/")
        x = int(x)
        y = int(y)
        percentage = (x/y) * 100
    except (ValueError, ZeroDivisionError):
        sys.exit("Wrong value")
    else:
        return percentage, x, y


def gauge(percentage, x_int, y_int):
    if x_int > y_int:
        sys.exit("Wrong Value")
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"



if __name__ == "__main__":
    main()


# while True:
#     try:
#         x, y = input("Fraction: ").split("/")
#         x = int(x)
#         y = int(y)
#         percentage = (x / y) * 100
#     except (ValueError, ZeroDivisionError):
#         pass
#     else:
#         if x > y:
#             continue
#         elif percentage <= 1:
#             print("E")
#         elif percentage >= 99:
#             print("F")
#         else:
#             print(f"{int(percentage)}%")
#         break

