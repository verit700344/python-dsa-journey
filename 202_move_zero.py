numbers= list(map(int, input(" enter the numbers: ").split())
              )
left = 0
for right in range(len(numbers)):
    if numbers[right] != 0:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
    elif numbers[right] == 0:
        continue
print("The numbers after moving zeros to the end are: ", numbers)