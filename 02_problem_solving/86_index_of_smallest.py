numbers = [10, 25, 7, 40, 18]

smallest = numbers[0]
smallest_index = 0

for i in range(len(numbers)):
    if numbers[i]< smallest:
        smallest = numbers[i]
        smallest_index = i

print(smallest_index)