numbers = [1, 1, 2, 2, 3, 4, 4]
left  = 0
right = len(numbers) - 1
left = 0

for right in range(1, len(numbers)):
    if numbers[right] != numbers[left]:
        left += 1
        numbers[left] = numbers[right]
print(numbers[:left + 1])