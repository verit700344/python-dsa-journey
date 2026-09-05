numbers = list(map(int, input(" enter the numbers: ").split()))
target = int(input(" enter the target: "))
left = 0
found = False
right = len(numbers) - 1
while left < right:
    if numbers[left] + numbers[right] < target:
        left += 1
    elif numbers[left] + numbers[right] > target:
        right -= 1
    else:
        print(f"Pair found: ({numbers[left]}, {numbers[right]})")
        found = True
        left += 1
        right -= 1
if not found:
    print("No more pairs found.")