numbers = [1, 2, 3, 4, 5, 6, 7, 8]
target = 9

left = 0
right = len(numbers) - 1
found = False 

while left < right:
    total = numbers[left]+ numbers[right]
    
    if total == target:
                           
            print(numbers[left],numbers[right])

            left += 1
            right -= 1

    
    
        
    elif total < target:
        left += 1
    else :
          right -= 1
          
