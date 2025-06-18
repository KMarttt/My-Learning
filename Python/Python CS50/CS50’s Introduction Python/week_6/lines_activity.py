def file_check(file_name):

    split_word = file_name.split()
    word_count = len(split_word)

    if word_count == 0:
        print("Too few command-line argument")
        return False
    elif word_count >= 2:
        print("Too many command-line argument")
        return False
    elif file_name.endswith(".py") == False:
        print("Not a python file")
        return False

    try:
        with open (file_name) as file:
            pass
    except:
        print("Wrong file")
    else:
        return True

file_name = input("Input file_name: ").strip()
if file_check(file_name):
    with open(file_name) as file:
        # lines = file.readlines()

        # always remember readlines || with s

        # i= 0
        # for y in lines:
        #     if y.startswith("# ") or y == "\n":
        #         # \n is used because the code itself is copied when u used readline
        #         continue
        #     else:
        #         i+= 1
        # print(i)

        """ OR  """

        i = 0
        for line in file:
            if line.startswith("# ") or line == "\n":
                # \n is used because the code itself is copied when u used readline
                continue
            else:
                i+=1
        print(i)