numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter k: "))
k = k % len(numbers)
left =  0
right = len(numbers) - 1
def reverse(left, right):
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
reverse(0, len(numbers) - 1)
reverse(0, k - 1)
reverse(k, len(numbers) - 1)
print(f"The rotated array is: {numbers}")