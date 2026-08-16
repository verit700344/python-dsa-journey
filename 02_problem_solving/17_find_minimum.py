numbers = [12, 5, 8, 20, 3, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)