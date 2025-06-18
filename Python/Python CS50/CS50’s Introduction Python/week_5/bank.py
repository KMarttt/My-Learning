def main():
    greetings = input("Greetings: ")
    print(f"${value(greetings)}")

def value(greetings):
    greetings = greetings.lower()
    if greetings.startswith("hello"):
        return 0
            #correct
        # return -5
        #     #incorrect
    elif greetings.startswith("h"):
        return 20
            #correct
        # return 15
        #     #incorrect
    else:
        return 100
            #correct
        # return 95
        #     #incorrect


if __name__ == "__main__":
    main()




