# arithmetic operation using a menu-driven approach
'''import sys
def addition(a, b):
    return a + b

def subtraction(a, b):
    return (a-b)

def multiplication(a, b):
    return (a*b)

def division(a, b):
    return (a/b)

while True:
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    choice = int(input("\nEnter your choice: "))
    if choice == 5:
        print("Exited")
        sys.exit()
    else:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if choice == 1:
            print("Addition: ", addition(a, b))
        elif choice == 2:
            print("Subtraction: ", subtraction(a, b))
        elif choice == 3:
            print("Multiplication: ", multiplication(a, b))
        else:
            print("Division: ", a/b)

        print("------------")'''

'''# Nested functions
def outer_function():
    print("This is my outer function")
    def inner_function():
        print("This is the inner function")
    inner_function()

outer_function()

# count word
text = input("Enter a sentence: ")
newText = text.split(" ")
#print(newText)
print("Word count: ", len(newText))'''

tupleA = 'a', 'b'
tupleB = ('a', 'b')
print(tupleA == tupleB)

# #
# 1. Tuple Concatenation
# #
init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print("Tuple Concatenation:", init_tuple_a + init_tuple_b)


# #
# 2. Tuple vs String Trick
# #
init_tuple = ('Python') * 3
print("Type of init_tuple:", type(init_tuple))  # str


# #
# 3. String replace() examples
# #
s = ""
s1 = s.replace("difficult", "easy")
print("Replace in empty string:", s1)

s = "ababababababab"
s1 = s.replace("a", "b")
print("Replace all 'a' with 'b':", s1)


# #
# 4. City Input Program
# #
city = input("Enter your city name: ")
scity = city.strip().lower()

if scity == "hyderabad":
    print("Hello Hyderabadi... Adab")
elif scity == "chennai":
    print("Hello Madrasi... Vanakkam")
elif scity == "bangalore":
    print("Hello Kannadiga... Shubhodaya")
else:
    print("Your entered city is invalid")


# #
# 5. List Comprehension (Even Numbers)
# #
# Case 1: list of integers
s = [1, 2, 3, 4, 5, 6]
val2 = [i for i in s if i % 2 == 0]
print("Even numbers from list:", val2)

# Case 2: string input
s = "123456"
val2 = [i for i in s if int(i) % 2 == 0]
print("Even digits from string:", val2)

#  dictionary compression
squares = {x: x*x for x in range(1, 6)}  # x = 1
print(squares)
