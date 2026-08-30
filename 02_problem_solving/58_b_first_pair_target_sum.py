numbers = [1, 2, 4, 6, 8]
target = 10
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
            found = True
            break

    if found:
        break
