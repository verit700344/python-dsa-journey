numbers = [3, -2, 5, -1, 4, -6]

left = 0
right = len(numbers) - 1

while left < right:

    if numbers[left] < 0:
        left += 1

    elif numbers[right] >= 0:
        right -= 1

    else:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1

print(numbers)