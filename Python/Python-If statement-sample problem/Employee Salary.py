# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


salary=int(input("Salary: "))
year_of_service=int(input("Year of Service: "))

if year_of_service > 5:
    net_bonus=salary * 0.05
    print("Net bonus amount: " + str(net_bonus))
else:
    print("No Bonus")


# Answer from the internet (with my own optimization)

salary=int(input("Salary: "))
yos=int(input("Year of Service: "))

if yos > 5:
    print ("Bonus is",.05*salary)
else:
    print ("No Bonus")

# Lesson Learned:
    # You can combine print with an operation, just use (,)
        # print ("Bonus is",.05*salary)
    # You may also use (+), but the operation needs to be str() - much more work
        # print ("Bonus is" + str(.05*salary))

# So i guess, (+) concatenate a data (combining) 
# while (,) is simply adding a data ( so all type of data is applicable)