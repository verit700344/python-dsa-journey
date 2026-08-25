numbers = [3, 8, 12, 5, 18, 21, 24, 7]

low = 8
high = 20
largest = 0

for number in numbers:
   if number >= low and number <= high and number % 2 == 0:
       if number > largest:
          largest= number

print(largest)
