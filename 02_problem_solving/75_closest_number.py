numbers = [10, 20, 30, 40, 50]
target = 26

closest = numbers[0]

for number in numbers:
    if abs(number - target) < abs(closest - target):
        closest = number

print(closest)