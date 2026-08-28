numbers = [1, 1, 2, 2, 2, 3, 4, 4]

current = 1
largest = 1

for i in range(1, len(numbers)):

    if numbers[i] == numbers[i - 1]:
        current += 1
    else:
        current = 1

    if current > largest:
        largest = current

print(largest)