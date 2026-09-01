numbers = [3, 5, 2, 8, 1, 4]

stack = []

for number in numbers:

    if not stack:
        stack.append(number)

    else:
        if number < stack[-1]:
            stack.append(number)
        else:
            stack.append(stack[-1])

print(stack)