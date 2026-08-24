numbers = [4, 7, 2, 9, 5, 12]
target = 6

last_greater = None

for number in numbers:
    if number > target:
        last_greater = number

print(last_greater)