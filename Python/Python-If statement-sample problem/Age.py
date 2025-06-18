#NEED TO BE OPTIMIZED
#Does not consider when all the age is equal (or 2 age is equal)
#Still gives a slightly correct answer, but I want it to give an absolute correct answer on all possible given
# i.e Person (2) and Person (3) is the youngest
# Also try to decrease the line of codes


#Take input of age of 3 people by user and determine oldest and youngest among them.

age1=int(input("Enter the Age of Person (1): "))
age2=int(input("Enter the Age of Person (2): "))
age3=int(input("Enter the Age of Person (3): "))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if age1 >= age2 and age1 >= age3:
    print("Oldest: Person (1) with the age of", age1)
elif age2 >= age1 and age2 >= age3:
    print("Oldest:  Person (2) with the age of", age2)
elif age3 >= age1 and age3 >= age2:
    print("Oldest: Person (3) with the age of", age3)



if age1 <= age2 and age1 <= age3:
    print("Youngest: Person (1) with the age of", age1)
elif age2 <= age1 and age2 <= age3:
    print("Youngest: Person (2) with the age of", age2)
elif age3 <= age1 and age3 <= age2:
    print("Youngest: Person (3) with the age of", age3)




