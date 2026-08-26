numbers = [6, 8, 9, 12, 15, 18, 20, 24]
count = 0

for number in numbers:
   if number % 2 == 0 and number % 3 == 0:
        count += 1

print(count)