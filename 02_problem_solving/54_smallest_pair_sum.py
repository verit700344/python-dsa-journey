numbers = [3, 7, 2, 9, 5]

smallest_pair = numbers[0] + numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair_sum = numbers[i] + numbers[j]

        if pair_sum < smallest_pair:
            smallest_pair = pair_sum

print(smallest_pair)