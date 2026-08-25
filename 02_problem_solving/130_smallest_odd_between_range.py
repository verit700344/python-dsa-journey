numbers = [3, 8, 11, 5, 18, 21, 7, 24]

low = 8
high = 22
smallest = numbers[0]

for number in numbers:
   if number >= low and number <= high and number % 2 != 0:
       if number < smallest:
          smallest = number

print(smallest)
