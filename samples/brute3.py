numbers = [10, 20, 10, 30, 20, 10, 40]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1
print(frequency)

