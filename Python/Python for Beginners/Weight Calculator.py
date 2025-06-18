weight = float(input("Weight: "))
K_L = input("(K)g or (L)bs: ").upper()      #Unit
                                            #Upper the input in order to properly compare it


if K_L == "K":  #remember to use ("") on K since it is a string
                # also  use (==) since we are comparing and not assigning a value to a variable
    lbs = weight / 0.45
    print("Weight in lbs: " + str(lbs))
elif K_L == "L":
    kg = weight * 0.45
    print("Weight in lbs: " + str(kg) )
else:
    print("error")