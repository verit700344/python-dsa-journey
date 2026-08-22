numbers = [1, 2, 2, 3, 4, 3, 5, 1]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print(result)