numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
target = int(input("Enter the target number: "))

left = 0
right = len(numbers) - 1
last = -1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        last = mid
        left = mid + 1  # Move right to find the last occurrence

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print("Last occurrence:", last)