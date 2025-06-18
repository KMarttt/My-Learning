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

old_csv, new_csv = file_checker(input_file)

with open(old_csv) as reading_old_file:
    lines = []
    i = 0
    for line in reading_old_file:
        row = []
        item = line.split(",")
        if i == 0:
            row = [item[0], item[1].removesuffix("\n")]
            lines.append(row)
            print(lines)
        else:
            item[0] = item[0].lstrip('"').rstrip()
            item[1] = item[1].lstrip().rstrip('"')
            item[2] = item[2].rstrip("\n")
            row = [item[0], item[1], item[2]]
            lines.append(row)
        i +=1
    print(lines)



with open(new_csv, "a") as writing_new_file:
    for x in lines:
        for y in x:
            text =



    # Approach
    # 3 conditional

    for x in lines:
        writing_new_file.write(x)

"""lesson learned: split(,) don't give a fuck about strings, it just split them whether they are 
 string or simply a symbol used to partition items"""
"""They don't accept list"""



