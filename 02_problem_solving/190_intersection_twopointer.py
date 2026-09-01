numbers1 = [1, 2, 4, 5, 6]
numbers2 = [2, 4, 6, 8]
left = 0
right = 0

result = []

while left < len(numbers1) and right < len(numbers2):

    if numbers1[left] == numbers2[right]:
        result.append(numbers1[left])
        left += 1
        right += 1

    elif numbers1[left] < numbers2[right]:
        left += 1

    else:
        right += 1
print(result)