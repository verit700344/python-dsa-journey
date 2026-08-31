numbers = [2, 1, 5, 3, 4]

stack = []
result = [-1] * len(numbers)

for i in range(len(numbers)):

    while stack and numbers[i] > numbers[stack[-1]]:
        
       result[stack[-1]] = numbers[i]
       stack.pop()

    stack.append(i)

print(result)