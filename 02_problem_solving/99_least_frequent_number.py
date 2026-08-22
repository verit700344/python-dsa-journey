numbers = [1, 2, 2, 3, 2, 4, 3]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

smallest = float("inf")
least_frequent = 0

for number in frequency:
    if frequency[number] < smallest:
        smallest = frequency[number]
        least_frequent = number

print(least_frequent)