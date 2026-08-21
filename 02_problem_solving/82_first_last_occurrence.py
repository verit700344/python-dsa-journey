numbers = [4, 2, 7, 2, 9, 2, 5]
target = 2

first = -1
last = -1

for i in range(len(numbers)):
    if numbers[i] == target:

        if first == -1:
            first = i

        last = i

print(first)
print(last)