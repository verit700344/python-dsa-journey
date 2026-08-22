numbers = [1, 2, 2, 3, 2, 4, 3]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

largest = 0
most_frequent = 0

for number in frequency:
    if frequency[number] > largest:
        largest = frequency[number]
        most_frequent = number

print(most_frequent)