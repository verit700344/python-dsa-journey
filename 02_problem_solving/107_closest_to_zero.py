
numbers = [-10, -3, 5, 8, -2, 7]

closest = numbers[0]

for number in numbers:
    if abs(number) < abs(closest):
        closest = number

print(closest)