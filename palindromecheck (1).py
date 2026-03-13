
name=input("Enter the string to check : ")
reversed_name=""
for i in name:
    reversed_name=i+reversed_name
print(reversed_name)
if(reversed_name==name):
     print("palindrome")
else:
     print("not palindrome")

