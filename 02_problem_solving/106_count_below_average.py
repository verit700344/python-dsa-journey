numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    if number != 0:
        total += number
        

average = total / len(numbers)

count = 0

for number in numbers:
    if number < average:
        count += 1

print(count)