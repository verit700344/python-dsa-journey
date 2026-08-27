numbers = [1, 2, 3, 4, 6, 8]
target = 10
left = 0
right = len(numbers) - 1

while left < right :
    total = numbers[left] + numbers[right]
    
    if total == target :
        print(left, right)
        break

    
    elif total < target:
        left += 1

    else:
        right -= 1
    