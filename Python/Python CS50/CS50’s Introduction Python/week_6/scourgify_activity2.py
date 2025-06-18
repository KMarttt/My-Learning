import csv
import sys

def file_checker(file_to_be_checked):
    word_count = len(file_to_be_checked.split())

    if word_count <= 1:
        sys.exit("To few command-line argument")
    elif word_count >= 3:
        sys.exit("To many command-line argument")

    old_csv, new_csv = file_to_be_checked.split()


    if old_csv.endswith(".csv") == False or new_csv.endswith(".csv") == False:
        sys.exit("Wrong file format")

    try:
        with open(old_csv) as file:
            pass
    except:
        sys.exit("No Old file found")
    else:
        return old_csv, new_csv


try:
    input_file = input("Input csv file (old and new): ")
except ValueError:
    sys.exit("Incorrect number of input")

new_csv_data = []
old_csv, new_csv = file_checker(input_file)
with open(old_csv) as reading_old_file:
    dict_csv = csv.DictReader(reading_old_file)

    for line in dict_csv:
        first, last = line["name"].split(",")
        last = last.lstrip()
        house = line["house"].rstrip("\n")
        new_csv_data.append({"first": first, "last": last, "house": house})



with open(new_csv, "w", newline='') as writing_old_file:
    print(new_csv_data)
    writer = csv.DictWriter(writing_old_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for x in new_csv_data:
        writer.writerow({"first": x["first"], "last": x["last"], "house": x["house"]})

