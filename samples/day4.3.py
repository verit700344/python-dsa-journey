def min_size_subarray(arr,target):
    left=0
    current_sum=0
    min_length=float('inf')

    for right in range(len(arr)):
        current_sum +=  arr[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return 0 if min_length == float("inf") else min_length