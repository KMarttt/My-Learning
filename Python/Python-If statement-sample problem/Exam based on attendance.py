#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

print("Exam permission based on Attendance")

# ch = class held; ca=class attended
ch=int(input("Number of clsses held: "))
ca=int(input("Number of class attended: "))

# p_ca = percentage of class attended
p_ca=(ca/ch)*100

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if p_ca < 75:
    print("No Exam")
else:
    print("You are allowed to take your Exam")
