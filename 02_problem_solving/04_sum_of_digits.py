number = 12345
total = 0

while number > 0:
    digit = number % 10
    total = total + number
    number = number // 10
print(total)