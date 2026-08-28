numbers = [1, 2, 3, 4, 6, 7, 8]
left = 0
right = len(numbers) - 1
while left < right:
    while numbers[left] % 2 != 0:
       left += 1

    while numbers[right] % 2 != 0:
       right -= 1
         
    numbers[left], numbers[right] = numbers[right], numbers[left]
    right-=1
    left += 1
print(numbers)