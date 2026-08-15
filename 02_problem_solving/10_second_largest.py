numbers = [10, 25, 7, 42, 18]
largest = numbers[0]
second_largest = numbers[0]
for number in numbers:
    if number > largest:
      second_largest = largest
      largest = number
    elif number > second_largest:
      second_largest = number
print(second_largest)
print(largest)