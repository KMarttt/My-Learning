""" 2 lists to dictionary"""

"""My Code"""
# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]
# dictionary = {}
#
# for x in range (0,len(keys)):
#     dictionary[keys[x]] = values[x]
#
# print(dictionary)

"""Code there"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

# this thing used zip function