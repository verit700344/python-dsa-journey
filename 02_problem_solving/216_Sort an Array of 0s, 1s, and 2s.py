numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
low = 0
mid = 0
high = len(numbers) - 1
# dutch national flag algorithm
while mid <= high:
    if numbers[mid] == 0:
        
        numbers[low], numbers[mid] = numbers[mid], numbers[low]
        low += 1
        mid += 1

    elif numbers[mid] == 1:
        # just move mid
        mid += 1

    elif numbers[mid] == 2:
        numbers[mid], numbers[high] = numbers[high], numbers[mid]
        high -= 1
     
print("Numbers after sorting:", numbers)
#good