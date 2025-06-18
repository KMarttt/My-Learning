# command=input("> ").lower()
#
# while command != "quit":
#     if command == "help":
#         print(stop - to stop the car")
#         print("start - to start the car")
#         print("quit - to exit")
#         print()
#         command = input("> ").lower()
#
#     elif command == "start":
#         print("Car started...Ready to go!")
#         command = input("> ").lower()
#         while command == "start":
#             print("The car has already started")
#             command = input("> ").lower()
#
#     elif command == "stop":
#         print("Car stopped.")
#         command = input("> ").lower()
#         while command == "stop":
#             print("The car has already stopped")
#             command = input("> ").lower()
#     else:
#         print("I don't understand that...")
#         command = input("> ").lower()

# problem with this: too long

print("THE CAR GAME")
print("~~~~~~~~~~~~~~~~~~~~~")
print("Tip: type help for the commands")
print()

started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        print()

    elif command == "start":
        if started == True:
            print("The car has already started")
        else:
            print("Car started...Ready to go!")
            started = True

    elif command == "stop":
        if started == True:
            print("Car stopped.")
            started = False
        else:
            print("The car is already stopped")

    elif command == "quit":
        break

    else:
        print("I don't understand that...")
