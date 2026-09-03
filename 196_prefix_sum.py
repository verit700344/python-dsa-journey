numbers = list(map(int, input("Enter numbers: ").split()))
limit = int(input("Enter range: "))

# Build prefix sum array
prefix = [0] * (len(numbers) + 1)  # extra 0 at start
for i in range(len(numbers)):
    prefix[i + 1] = prefix[i] + numbers[i]

print("Prefix array:", prefix)

# Query
left = int(input("Enter left index: "))
right = int(input("Enter right index: "))

# Range sum from left to right (inclusive)
range_sum = prefix[right + 1] - prefix[left]
print("Range sum:", range_sum)
