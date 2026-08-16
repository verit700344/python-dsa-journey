numbers = [12, 5, 8, 20, 3, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)