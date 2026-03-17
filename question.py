input = [1, 2, 3, 4]
answer = []

product = 1
for i in range(0, len(input)):
    product =  product * input[i]
    answer[i] = product / input[i]

print(answer)