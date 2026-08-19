numbers = [10, 5, 20, 8, 15]

smallest = numbers[0]
sec_smallest = numbers[0]
for number in numbers:
    if number < smallest:
        sec_smallest = smallest
        smallest = number
    elif number < sec_smallest:
        sec_smallest=number
print(sec_smallest)