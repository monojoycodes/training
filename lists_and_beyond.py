# day 2!
       #     0         1    2      3  
my_list = ["Monojoy", 20, 40.34, True]
#            -4      -3   -2      -1

'''
for i in range(0, len(my_list)):
    print(my_list[i])
'''

'''print(my_list[1:3])
print(my_list[:3])
print(my_list[1:3:2])'''

# Stacks and Queues are represented by Lists in Python!
"""my_list.append("Olly")
my_list.append("Swap")
my_list.append(69)
my_list.pop()
my_list.insert(1, "Swapnil")

new_list = my_list.copy()

print(new_list)"""

# 2D Lists

"""record = [ 
    ["Monojoy", 20],
    ["Swapnil", 21],
    ["Blah blah", 22]
]

print(record[0][0])
print(record[2][0])
print(record[2][1])
print(record[0][1])"""

# del my_list[4]
# print(my_list)

"""list2 = my_list.copy()
print("list2: ",list2)
list2.clear()
print("list2: ",list2)"""

"""name = "Monojoy"
my_name = list(name)

print(name)
print(my_name)"""

# Sort: HeadsUp! Python3 cannot sort heterogenous lists.
"""nums = [32,65,34,66,2,67,25,6]
nums.sort()
print(nums)

nums.sort(
    reverse=True
) # reverse

print(nums)"""

# id(var) is used to return the address of a variable
"""math = 3.14
PI = 3.14
print(id(math))
print(id(PI))

if (id(math) == id(PI)):
    print("SAME")"""

"""number = [2,5,6,4,6,73,3]
newnumber = number
"""
"""if (id(number) == id(newnumber)):
    print("SAME")""" # using .copy() will NOT have same memory addr


### If a value already exists in a memory then new address is not created!!!

