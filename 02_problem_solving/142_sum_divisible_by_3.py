numbers = [3, 7, 9, 12, 14, 18, 20, 21]

total = 0

for number in numbers:
    if number % 3 == 0:
        total += number

print(total)