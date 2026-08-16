numbers = [5, 12, 15, 20, 22, 25, 31, 40]

count = 0

for number in numbers:
    if number % 5 == 0:
        count += 1

print(count)