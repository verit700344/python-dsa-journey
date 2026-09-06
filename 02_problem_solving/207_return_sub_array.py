

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
current_sum = numbers[0]
maximum_sum = numbers[0]
start = 0
best_start = 0
best_end = 0
for index, number in enumerate(numbers[1:], start=1):
        if current_sum + number < number:
            current_sum = number
            start = index
        else:
            current_sum += number

        if current_sum > maximum_sum:
            maximum_sum = current_sum
            best_start = start
            best_end = index
print("Subarray:", numbers[best_start:best_end + 1])
print("Maximum sum:", maximum_sum)