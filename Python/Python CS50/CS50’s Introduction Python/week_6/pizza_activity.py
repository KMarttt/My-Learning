import csv

from tabulate import tabulate

def file_checker(file_to_be_checked):
    word_count = len(file_to_be_checked.split())

    if word_count == 0:
        print("Too few command-line arguments")
        return False
    elif word_count >= 2:
        print("Too many command-line arguments")
        return False
    elif file_to_be_checked.endswith(".csv") == False:
        print("Not a CSV File")
        return False

    try:
        with open (file_to_be_checked) as file:
            pass
    except:
        print("No CSV File found")
    else:
        return True


input_csv_file = input("Enter a CSV file to input: ")

if file_checker(input_csv_file):
    with open(input_csv_file) as file:
        reader = csv.reader(file)
        table = []
        for line in reader:
            row = [line[0], line[1], line[2].removesuffix("\n")]
            table.append(row)

        print(tabulate(table, headers="firstrow", tablefmt="grid"))

# as you can see here, the csv.reader converts the text into a list with the
#  comma (,) acting as the partition for the following
# so you no longer need to split the following using .split(,) and storing them into a list



