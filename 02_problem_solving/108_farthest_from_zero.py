numbers = [-10, -3, 5, 8, -2, 7]
farthest = numbers[0]
for number in numbers:
    if abs (number) > abs(farthest):
        farthest = number

print(farthest)
