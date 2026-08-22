numbers1 = [1, 2, 2, 3, 4, 4]
numbers2 = [2, 3, 4, 5]
common = [ ]
for number in numbers1:
    if number in numbers2 and number not in common:
        common.append(number)

print(common)

