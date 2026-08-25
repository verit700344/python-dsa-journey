numbers = [2, 8, 5, 12, 7, 16, 3]
target = 6
count = 0
for number in numbers:
    if number < target and number % 2 != 0:
        count+= 1
print(count)