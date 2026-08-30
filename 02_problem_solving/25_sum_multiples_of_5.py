numbers = [5, 12, 15, 20, 22, 25, 31, 40]

total = 0

for number in numbers:
    if number % 5 ==0:
        total = total + number

print(total)
