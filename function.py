# function
'''def msg():
    print("Hello World!!!!!!")
msg()'''

# Return multiple values
'''def maths():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return sum, sub, mul, div

print(maths())'''

# types of arguments that can be passed- 
# # Positional, Keyword, default, variable-length arg / variable no. of argument

# 1. Positional
def personalInfo(first_name, last_name):
    print(first_name, last_name)

print(personalInfo("Monojoy", "Dey"))