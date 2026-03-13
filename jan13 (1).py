# 1  5
# 2  4
# 4  2
# 5  1
for i in range(1,6):
        if i==3 :

            continue
        print(i," ",6-i)

# ## using while loop
# i=1
# while i<=5: 
#     if i==3:
#         i=i+1
#         continue
#     print(i," ",6-i)
#     i=i+1

# # 
# username=""
# password=""

# while username!="admin" and password!="1234":
#     username=input("Enter username:")
#     password=input("Enter password:")


# n=int(input("Enter a number:"))
# sum=0  
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1       
# print("Sum of first",n,"numbers is",sum)


# name="monojoy"

# #o/p= m o n j  y
# #  remove duplicate
# newname=""
# for i in name:
#     if i not in newname:
#         newname=newname+i


# print(newname)
#wap to reverse a string using any loop
# name="monojoy"
# reversed_name=""
# for i in name:
#     reversed_name=i+reversed_name
# print(reversed_name)


# mycart=[10,200,300,800,60,700]
# for i in mycart:
#       if i>400:
#        print("this is my purchased cart item")
#       continue
# print(i)


name=input("Enter the string to check : ")
reversed_name=""
for i in name:
    reversed_name=i+reversed_name
print(reversed_name)
if(reversed_name==name):
     print("palindrome")
else:
     print("not palindrome")


