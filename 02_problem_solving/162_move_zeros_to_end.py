numbers = [0, 1, 0, 3, 12]

left = 0

for right in range(len(numbers)):
    if numbers[right] != 0:
        numbers[left] = numbers[right]
        left += 1

for right in range(left, len(numbers)):
    numbers[right] = 0

print(numbers)