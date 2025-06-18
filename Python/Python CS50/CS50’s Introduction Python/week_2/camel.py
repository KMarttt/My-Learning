camel_case = input("Camel Case: ")
snaking_case = ""

snaking_case = ""
for char in camel_case:
    if char.isupper() == True:
        lowered_char = char.lower()
        new_char = "_" + lowered_char
        snaking_case+= new_char
    else:
        snaking_case+= char


print(snaking_case)
