numbers = [4, 6, 7, 9, 10, 11, 12, 13]
count = 0

for number in numbers:
   if number % 2 == 0 or number % 3 == 0:
        count += 1

print(count)