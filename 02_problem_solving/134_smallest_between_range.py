numbers = [2, 15, 8, 22, 17, 30, 12]

low = 10
high = 25
smallest = numbers[0]

for number in numbers:
    if number >= low and number <= high:
        if number < smallest:
         smallest = number
print(smallest) 