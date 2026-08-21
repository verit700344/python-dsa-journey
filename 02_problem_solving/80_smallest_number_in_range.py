numbers = [2, 15, 8, 22, 17, 30, 12]
low = 10
high = 20
smallest = None

for number in numbers:
    if number >= low and number <= high:
        if smallest is None or number < smallest:
            smallest = number

print(smallest)