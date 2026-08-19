numbers = [8, 3, 6, 2, 9]

smallest_sum = numbers[0] + numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] < smallest_sum:
            smallest_sum = numbers[i] + numbers[j]
            
            
print(smallest_sum)
