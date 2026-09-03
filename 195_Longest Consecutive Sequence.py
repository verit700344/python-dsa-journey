numbers = list(map(int, input("Enter numbers: ").split()))
numbers_set = set(numbers)

longest = 0

for number in numbers_set:
    # decide whether this is the beginning
    if number - 1 not in numbers_set:
        current = number
        count = 1
        # count the consecutive sequence
        while current + 1 in numbers_set:
            current += 1
            count += 1
        # update longest
        longest = max(longest, count)

print(longest)