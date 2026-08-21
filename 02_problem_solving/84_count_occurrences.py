numbers = [4, 2, 7, 2, 9, 2, 5]
target = 2

count = 0

for i in range(len(numbers)):
    if numbers[i]== target:
        count += 1

print(count)