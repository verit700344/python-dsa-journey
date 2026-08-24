numbers = [10, 8, 12, 5, 7, 3]
target = 6

count = 0

for number in numbers:
    if number < target:
        count += 1

print(count)