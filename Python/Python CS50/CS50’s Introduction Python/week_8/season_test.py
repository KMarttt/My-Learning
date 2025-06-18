from datetime import date
import sys
import inflect

# def date_checking(check_date):
#     date_component = check_date.split("-")
#
#     int_date_component = []
#     # index: 0 = year, 1 = months, 2 = days
#     try:
#         for component in date_component:
#             int_date_component.append(int(component))
#     except ValueError:
#         sys.exit("Invalid Date Format")
#
#     if int_date_component[0] < 999:
#         # check if year is less than 999 = INVALID
#         sys.exit("Invalid Year")
#     elif int_date_component[1] > 12 or int_date_component[1] < 0:
#         # check if month is greater than 12 or less than 0 = INVALID
#         sys.exit("Invalid Month")
#     elif int_date_component[2] > 31 or int_date_component[2] < 0:
#         # check if day is greater than 31 or less than 0 = INVALID
#         sys.exit("Invalid Day")





def main():
    inputted_date = input("Date of Birth: ").strip()
    p = inflect.engine()
    try:
        # formats it to datetime.date
        formated_date = date.fromisoformat(inputted_date)
    except ValueError:
        sys.exit("Invalid Date")
    # print(type(inputted_date))
    # print(formated_date)
    # print(type(formated_date))


    date_today = date.fromisoformat("2000-01-01")   #date.today()
    # print(date_today)
    # print(type(date_today))

    time_alive = date_today - formated_date
    # print(time_alive)

    time_alive_min= (time_alive.total_seconds())/60
    # print(int(time_alive_min))

    print(p.number_to_words(int(time_alive_min)).capitalize())






if __name__ == "__main__":
    main()