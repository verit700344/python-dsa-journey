numbers = [7, 2, 9, 4, 1, 6]

largest = numbers[0]
smallest = numbers[0]
for number in numbers :
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number 

print(largest - smallest)