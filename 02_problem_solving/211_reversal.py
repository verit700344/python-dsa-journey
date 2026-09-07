numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter k: "))
k = k % len(numbers)
left =  0
right = len(numbers) - 1
left = 0
right = len(numbers) - 1

while left < right:
    # swap numbers[left] and numbers[right]
    numbers[left], numbers[right] = numbers[right], numbers[left]
    # move both pointers
    left += 1
    right -= 1
print("Reversed numbers:", numbers)