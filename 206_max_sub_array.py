numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
current_sum = numbers[0]
maximum_sum = numbers[0]
for number in numbers:
    current_sum = max(number, current_sum + number)
    maximum_sum = max(maximum_sum, current_sum)
print("Maximum contiguous subarray sum is:", maximum_sum)