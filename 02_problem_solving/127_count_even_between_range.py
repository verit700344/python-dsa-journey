numbers = [2, 5, 8, 12, 15, 18, 20, 23]
low = 8
high = 20
count = 0

for number in numbers:
   if number >= low and number <= high and number % 2 == 0:
        count += 1

print(count)