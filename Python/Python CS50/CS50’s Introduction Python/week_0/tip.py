def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = d.removeprefix("$")
    dollar_float = float(dollar)
    return dollar_float


def percent_to_float(p):
    percentage = p.removesuffix("%")
    percent_float = float(percentage)/100
    return percent_float



main()