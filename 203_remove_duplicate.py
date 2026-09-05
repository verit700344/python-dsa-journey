numbers= list(map(int, input(" enter the numbers: ").split())
              )
left = 0
for right in range(1, len(numbers)):
    if numbers[right] != numbers[left]:
        left += 1
        numbers[left] = numbers[right]
print("The numbers after removing duplicates are: ", numbers[:left+1])