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

# 2. Keyword
def greet(name, age):
    print(f"{name} is {age} years old")

greet(name="Alice", age=25)
greet(age=30, name="Bob")  # order doesn't matter with keyword args

# 3. Default arguments
def introduce(name, country="USA"):
    print(f"{name} is from {country}")

introduce("Charlie")  # uses default country
introduce("Diana", "UK")  # overrides default

# 4. Variable-length arguments (*args for non-keyword, **kwargs for keyword)
def sum_numbers(*args):
    total = sum(args)
    print(f"Sum of {args} = {total}")

sum_numbers(1, 2, 3)
sum_numbers(10, 20, 30, 40)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Eve", age=28, city="NYC")

fruit = {}
def addone(idx):
    if idx in fruit:
        fruit[idx] =+ 1
    else:
        fruit[idx] = 1
addone("Apple")
addone("banana")
addone("apple")

print(len(fruit))
