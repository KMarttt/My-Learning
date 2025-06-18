def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 8>= converted_time >= 7:
        print("Breakfast Time")
    elif 13>= converted_time >= 12:
        print("Lunch Time")
    elif 19>= converted_time >= 18:
        print("Dinner Time")

def convert(to_convert_time):
    hours, minutes = to_convert_time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    converted_minutes = minutes/60
    converting_time = hours + converted_minutes
    return converting_time

if __name__ == "__main__":
    main()