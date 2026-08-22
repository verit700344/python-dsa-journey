numbers = [1, 4, 7, 2, 9, 6, 3]

result = []
for number in numbers:
    if number % 2 :
        result.append(number)

for number in numbers:
    if number % 2 == 0:
        result.append(number)


print(result)