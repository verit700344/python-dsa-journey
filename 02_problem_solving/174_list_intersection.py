numbers1 = [1, 2, 4, 6, 8]
numbers2 = [3, 4, 5, 6, 9]
seen = set(numbers1)
for number in numbers2:
    if number in seen:
        combined = numbers1 + numbers2
        
print(combined)      