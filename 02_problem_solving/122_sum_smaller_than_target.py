numbers = [10, 8, 12, 5, 7, 3]

target = 6

total = 0

for number in numbers:
    if number < target:
        total += number

print(total)