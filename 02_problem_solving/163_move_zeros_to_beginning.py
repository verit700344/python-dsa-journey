numbers = [0, 1, 0, 3, 12]

left = 0  # pointer for placing zeros at the beginning

for right in range(len(numbers)):
    if numbers[right] == 0:
        numbers[left] = 0
        left += 1

# Fill the rest with non-zero values
index = left
for right in range(len(numbers)):
    if numbers[right] != 0:
        numbers[index] = numbers[right]
        index += 1

print(numbers)
