from datetime import date
import sys
import inflect




def main():
    inputted_date = input("Date of Birth: ").strip()
    p = inflect.engine()
    try:
        # formats it to datetime.date
        formated_date = date.fromisoformat(inputted_date)
    except ValueError:
        sys.exit("Invalid Date")

    # gets the current date today (already in a datetime.date format)
    date_today = date.today()
    """if you want to check it using the time in the CS50"""
    # date_today = date.fromisoformat("2000-01-01")

    # subtract current day to birthday = time_alive
    time_alive = date_today - formated_date

    # converts the product to minutes
    time_alive_min= (time_alive.total_seconds())/60

    # print the time_alive_min in words with capitalized :stating letter
    # to round it to the nearest integers
    print(p.number_to_words(int(time_alive_min)).capitalize())

if __name__ == "__main__":
    main()