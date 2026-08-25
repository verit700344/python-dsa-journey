numbers = [2, 5, 8, 11, 14, 17, 20, 23]
low = 8
high = 20
total = 0

for number in numbers:
   if number >= low and number <= high and number % 2 != 0:
        total += number

print(total)
