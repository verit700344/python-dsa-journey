numbers = [4, -2, 7, -5, 9, -1, 3]

result = []

for number in numbers:
    if number < 0:
        result.append(number)
for number in numbers:
    if number >= 0 :
        result.append(number)

print(result)