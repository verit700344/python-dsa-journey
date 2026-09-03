def count_occurrences(arr, target):
    def first_occurrence():
        left, right, first = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def last_occurrence():
        left, right, last = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    first = first_occurrence()
    last = last_occurrence()
    return (last - first + 1) if first != -1 else 0

# Example
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3
