numbers = [10, 5, 20, 8, 15]

largest = numbers[0]
sec_largest = numbers[0]

for number in numbers:
    if number > largest:
        sec_largest = largest
        largest = number

    elif number > sec_largest:
        sec_largest = number

print(sec_largest)