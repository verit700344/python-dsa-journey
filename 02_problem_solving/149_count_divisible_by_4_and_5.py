numbers = [4, 5, 10, 15, 20, 25, 30, 40]
count = 0

for number in numbers:
   if number % 4 == 0 and number % 5 == 0:
        count += 1

print(count)