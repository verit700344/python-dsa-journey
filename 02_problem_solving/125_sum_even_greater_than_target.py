numbers = [2, 8, 5, 12, 7, 16, 3]
target = 6


total = 0

for number in numbers:
    if number > target and number % 2 == 0:
         total += number

print(total)