numbers = [2, 5, 7, 9, 12, 15]
target = 13
left = 0
right = len(numbers) - 1

closest_difference = float('inf')
closest_pair = ()

while left < right:
    total = numbers[left] + numbers[right]

    difference = abs(total - target)

    if difference < closest_difference:
        closest_difference = difference
        closest_pair = (numbers[left], numbers[right])

    if total < target:
        left += 1
    else:
        right -= 1
print(closest_pair)
