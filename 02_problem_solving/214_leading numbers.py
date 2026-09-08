numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
leading_number = numbers[0]
left = 0
right = len(numbers) - 1
leading_number = numbers[-1]
leaders = [leading_number]

right = len(numbers) - 2

while right >= 0:
    if numbers[right] > leading_number:
        leaders.append(numbers[right])
        leading_number = numbers[right]

    right -= 1
print("Leaders in the array:", leaders)