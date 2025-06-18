import inflect

p = inflect.engine()

name_list =[]
while True:
    name = input("Name: ")
    if name == "":
        break
    else:
        name_list.append(name)

join_names =p.join(name_list)
print(f"Adieu, adieu, to {join_names}")
