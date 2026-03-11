mark1 = int(input("Enter mark1: "))
mark2 = int(input("Enter mark2: "))
mark3 = int(input("Enter mark3: "))

total = mark1 + mark2 + mark3
maxmarks = 150
percentage = (total / maxmarks) * 100

if percentage > 60.00:
    print("You are Eligible! Percentage: ", percentage)
else:
    print("You are not eligible: ", percentage)

# check max
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))

greatest = num1

if num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    greatest = num2
if num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    greatest = num3
if num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    greatest = num4
if num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
    greatest = num5

print("Greatest number is:", greatest)
