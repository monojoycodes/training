# string slicing
name = "MonojoyDey"

'''print("name[1:8] :",name[1:8])
print("name[1:9:2] :",name[1:9:2])
print("name[-2:-9:-1] :",name[-2:-9:-1])
print("name[:8] :",name[:8])
print("name[::1] :",name[::1])
print("name[::-1] :",name[::-1])'''
# output
'''name[1:8] : onojoyD
name[1:9:2] : oooD
name[-2:-9:-1] : eDyojon
name[:8] : MonojoyD
name[::1] : MonojoyDey
name[::-1] : yeDyojonoM'''

'''quote = "Kindness is like snow, it beautifies everything it covers"
print(quote.find("beautifies")) # returns index of first occurance

# join method

print("Subject Marks: ")
phy, chem, math = 50, 60, 70
print("Physics = {} chemistry= {} maths={}".format(phy, chem, math))

total = phy + chem + math
print("total marks: ", f"{total}")'''

name = "MonojoyDey"
v = 0
c = 0
for i in name.lower():
    if i in ['a','e','i','o','u']:
        v+=1
    else:
        c+=1
print("vowels: ", v, "\nconsonants: ", c, "\nTotal: ",v+c)
    