numbers = [1, 2, 3, 4, 5]

first = numbers[0]

for i in range(0, len(numbers) - 1):
    numbers[i] = numbers[i + 1]

numbers[-1] = first

print(numbers)