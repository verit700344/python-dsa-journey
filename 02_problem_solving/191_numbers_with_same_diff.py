numbers = [1, 3, 5, 8, 10, 12]
target = 5
left, right = 0, len(numbers) - 1

while right < len(numbers):

    difference = numbers[right] - numbers[left]
    if difference == target:
        print(numbers[left], numbers[right])
        break
    elif difference < target:
        right += 1
    else:
        left += 1
    if left == right:
        right += 1
print("No pairs found with the given target difference.")