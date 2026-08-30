numbers = [1, 2, 2, 3, 4, 4, 5]

left = 0

for right in range(1, len(numbers)):

    if numbers[left] != numbers[right]:
        left += 1
        numbers[left] = numbers[right]
print(numbers[:left + 1])