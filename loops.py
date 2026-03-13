# Membership operators: [in, not in]
# Identity operators: [is, is not]

"""name = "Monojoy"
print("M" in name)
print("Z" not in name)"""

# For loop
'''for i in range(1,5, 2): #range(start,stop,step) stop -> non inclusive
    print(i) # 1, 3'''

"""for i in range(2, 14):
    print(i, "table\n ---------")
    for j in range(1, 11):
        print(i * j)
    print()

days = input("Enter the day: ")
if days == "SATURDAY" or "SUNDAY":
    print("WEEKEND")
else: 
    print("not a weekend")"""

#Day 3
'''for i in range(1,6):
    if i==3:
        continue
    print(i, " ", 6-i)

# another way:
for i, j in zip(range(1,6), range(5,0,-1)): # run multiple conditions- loop in once!
    if i == 3: 
        continue
    print(i, j)

# while
i = 1
while i<=5:
    print(i)
    i +=1
'''
name = "Monojoy"
# o/p = "Monjy"
newname= ""

'''for i in name:
    if (i in newname):
        continue
    newname = newname + i
print(newname)

for i in name:
    if i not in name:
        newname = newname + i
print(newname)'''

#Reverse a string using loop
'''name = "Monojoy"
#op = "yojonoM"
name = list(name)

for i, j in zip(range(0, len(name)), range(len(name)-1, 0, -1)):
    temp = name[i]
    name[i] = name[j]
    name[j] = temp
    
    if i > j:
        break
    
print(name)
        
# in string-
reversed_name = ""
for i in name:
    reversed_name = reversed_name + i
    print(reversed_name)
'''

# Palindromic 
'''name = "SWAPNIL"
if (name == name[::-1]):
    print("PALINDROME")
else:
    print("not a palindrome")
    '''

#anagram
word = "listen" #op = "silent"
another_word = "monojo"
word = list(word)
another_word = list(another_word)

word.sort()
another_word.sort()

for i in range(0, len(word)):
    if (word[i] == another_word[i]):
        flag = True
    else: 
        flag = False

if flag:
    print("ANAGRAM")
else:
    print("NOT ANAGRAM")