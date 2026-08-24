numbers = [5, -2, 8, -1, 3, -7, 4]

last_negative = None

for number in numbers:
    if number < 0 :
        last_negative = number

print(last_negative)