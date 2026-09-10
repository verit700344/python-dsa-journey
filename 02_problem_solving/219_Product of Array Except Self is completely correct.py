numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = [1] * len(numbers)
# Given an array, return a new array where each position contains the product of every other number, without using division.
for i in range(1, len(numbers)):
    result[i] = result[i - 1] * numbers[i - 1]

right_product = 1
for i in range(len(numbers) - 1, -1, -1):
    result[i] *= right_product
    right_product *= numbers[i]

print("Result:", result)