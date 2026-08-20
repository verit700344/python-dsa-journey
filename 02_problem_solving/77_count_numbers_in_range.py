numbers = [2, 5, 8, 12, 15, 18, 20]
low = 8
high = 18

range_count = 0
for number in numbers:
    if number >= low and  number <= high:
        range_count += 1

print(range_count)