numbers = [5, 8, 10, 12, 15, 17, 20, 23]

count = 0

for number in numbers:
    if number % 5 == 0:
        count += 1

print(count)