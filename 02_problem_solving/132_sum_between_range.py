numbers = [2, 5, 8, 12, 15, 18, 20, 25]

low = 8
high = 20

total = 0
for number in numbers:
    if number >= low and  number <= high:
        total += number
print(total)