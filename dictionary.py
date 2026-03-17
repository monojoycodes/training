my_dict = {
    "name":"Monojoy Dey",
    "professional": "developer",
    "empid": 1001
}
'''print(my_dict)
print(type(my_dict))'''

my_dict = {
    101: "Monojoy",
    "101": "Swapnil",
    102: "jacob",
    102: "Monojoy" # stored
}
for x in my_dict:
    print(x) #only unique keys: 101, 101, 102

for x in my_dict.values():
    print(x)


print()
# print keys and values both:
for x,y in my_dict.items():
    print(x,"- ", y)

# add new key as well as value-
my_dict["mob"] = 7448078000
print(my_dict)

# remove pair
my_dict.pop("mob")
print(my_dict)

