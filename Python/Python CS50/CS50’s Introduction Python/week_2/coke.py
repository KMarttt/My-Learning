def math_compute(cents, amount_due):
    # subtract amount with the paid cent
    answer = amount_due - int(cents)
    return answer


def input_cents(amount_due):
    # will only accept 5, 10, 25 cents
    while True:
        inputted_cents = int(input("Insert coin: "))
        if inputted_cents == 25 or inputted_cents == 10 or inputted_cents == 5:
            return inputted_cents
        else:
            print(f"Amount Due: {amount_due}")


def change_owed_compute(total_cent):
    # will subtract total cent (over 50) to the amount due to determine the change
    change_owed_compute = 50 - total_cent
    return change_owed_compute.__abs__()


total_cent = 0
amount_due = 50  # initial amount due
print(f"Amount Due: {amount_due}")  # will print the initial amount due
while True:
    if total_cent < 50:
        inputted_cents = input_cents(amount_due)    # will input 5/15/25 cents only
        amount_due = math_compute(inputted_cents, amount_due)   # subrtact inputted cents with the amount due
        total_cent += inputted_cents    # monitor the total cents inputted
    if total_cent < 50:
        print(f"Amount Due:{amount_due}")
    else:
        print(f"Change Owed:", change_owed_compute(total_cent))
        break
