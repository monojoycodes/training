'''element = input("Enter a username: ")
count = 0

for i in element:
    if (48 <= ord(i) <= 57) or (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        continue
    else:
        count += 1

print(count)

# using alphanum function is also possible!!'''

'''A = [1,2,3]
B = [2, 3, 4]
C = [3,4,5]

for i in A:
    if i in B and i in C:
        print(i)'''

# Move zeroes to end
# ip = [0, 1, 0, 3, 12]
# op = [1, 3, 12, 0, 0]

'''myList = [0, 1, 0, 3, 12]
for i in myList:
    if i == 0:
        myList.remove(i)
        myList.append(0)

print(myList)'''
        
        
    


