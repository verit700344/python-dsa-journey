numbers = [3, 7, 2, 9, 5]
largest_pair = 0

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] > largest_pair:
            largest_pair = numbers[i] + numbers[j]
print(largest_pair)