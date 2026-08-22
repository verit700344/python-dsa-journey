numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 4, 5, 6, 7]

result = []

for number in numbers1:
    if  number not in numbers2:
        result.append(number)

print(result)