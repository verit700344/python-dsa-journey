numbers = [1, 2, 3, 2, 4, 5]
target = 2

result = []

for number in numbers:
    if number != target:
        result.append(number)

print(result)