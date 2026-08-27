numbers = [2, 4, 5, 7, 9, 11]
target = 16


left = 0
right = len(numbers
            ) - 1
while left < right :
    total = numbers[left]+numbers[right]
    
    if total == target :
        print(left,right)
        break
    elif total < target:
        left += 1
    else :
        right -= 1