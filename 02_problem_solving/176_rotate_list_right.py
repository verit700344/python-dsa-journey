numbers = [1, 2, 3, 4, 5]

k = 2

numbers = numbers[-k:] + numbers[:-k]

print(numbers)