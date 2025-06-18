def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    year, month, day = get_date(months)
    print(f"{year}-{month:02}-{day:02}")


def get_date(months):
    while True:
        month, day, year = input("Date: ").replace("/", "-").replace(", ","-").replace(" ", "-").split("-")

        if month.isalpha() and day.isdigit() and year.isdigit():
            if month in months:
                int_month = months.index(month) + 1
            else:
                continue

            int_day = int(day)
            if int_day > 31:
                continue

            int_year = int(year)

            return int_year, int_month, int_day

        elif month.isdigit() and day.isdigit() and year.isdigit():
            int_month = int(month)
            if int_month > 12:
                continue

            int_day = int(day)
            if int_day > 31:
                continue

            int_year = int(year)

            return int_year, int_month, int_day
        else:
            continue


main()
