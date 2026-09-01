
numbers = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(numbers)):

    needed = target - numbers[i]

    if needed in seen:
        print(seen[needed], i)
        break

    seen[numbers[i]] = i
print(seen)