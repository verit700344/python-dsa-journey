numbers = [3, 7, 9, 12, 14, 18, 20, 21]

count = 0

for number in numbers:
    if number % 3 == 0:
        count += 1

print(count)