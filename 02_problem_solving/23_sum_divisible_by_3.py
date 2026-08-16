numbers = [3, 7, 9, 10, 12, 14, 18, 20]

total = 0

for number in numbers:
    if number % 3 == 0:
        total = total + number

print(total)