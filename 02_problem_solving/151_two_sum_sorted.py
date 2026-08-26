numbers = [1, 2, 3, 4, 6, 8]
target = 10

left = 0
right = len(numbers) - 1

if numbers[left] + numbers[right] == target:
    print(True)