numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

target_sum = int(input("Enter the target sum: "))
# Given an array of positive integers and a target sum, find the contiguous subarray whose sum equals the target.
current_sum = 0
start = 0

for end in range(len(numbers)):
    current_sum += numbers[end]

    while current_sum > target_sum:
        current_sum -= numbers[start]
        start += 1

    if current_sum == target_sum:
        print("Subarray found from index", start, "to", end)
        break
else:
    print("No subarray found with the given target sum.")