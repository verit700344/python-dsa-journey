numbers = [1, 2, 4, 7, 9]
target = 20

left = 0
right = len(numbers) - 1

found = False

while left < right:

    total = numbers[left] + numbers[right]

    if total == target :
           found = True
           break
        
    elif total < target:
            left += 1
    
    else:
            right -= 1
        
        

print(found)