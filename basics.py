# val1, val2 = 4, 2

# temp = val1
# val1 = val2
# val2 = temp

# print("Using temp: ",val1, val2)

# val1, val2 = 4, 2

# val1 = val1 + val2
# val2 = val1 - val2
# val1 = val1 - val2
# print("Using sum: ",val1, val2)

# val1, val2 = 4, 2

# val1 = val1 ^ val2
# val2 = val1 ^ val2
# val1 = val1 ^ val2
# print("Using Xor: ",val1, val2)


# Reverse a number:

num = 1234567
rev = 0
while (num > 0):
    last = num % 10
    num = num // 10
    rev = rev*10 + last
    print(rev)

