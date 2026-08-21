numbers = [10, 20, 30, 40, 50]
temp = numbers[0]


numbers[0] = numbers[-1]


numbers[-1] = temp
print(numbers)