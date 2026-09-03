numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
left = 0
right = len(numbers) - 1
target = int(input("Enter the target number to search for: "))
while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        print(f"Element found at index {mid}")
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")