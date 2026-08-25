numbers = [10, 5, 8, 3, 7, 12, 1]
target = 8

total = 0

for number in numbers:
    if number< target and number % 2 != 0:
        total += number

print(total)