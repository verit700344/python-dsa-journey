numbers = [4, 5, 4, 6, 5, 7, 6]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
for number in numbers:
    if frequency[number] == 1:
        print(number)
        break