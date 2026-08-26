numbers = [3, 8, 11, 14, 17, 20, 23, 26]

low = 10
high = 25
total = 0

for number in numbers:
    if number >= low and number <= high and number % 2 == 0:
        total += number
print( total) 