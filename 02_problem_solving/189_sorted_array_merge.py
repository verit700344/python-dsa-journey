numbers1 = [1, 3, 5, 7]
numbers2 = [2, 4, 6, 8]

left = 0
right = 0

result = []
while left < len(numbers1) and right < len(numbers2):

    if numbers1[left] < numbers2[right]:
        result.append(numbers1[left])
        left += 1
    else:
        result.append(numbers2[right])
        right += 1
while left < len(numbers1):
    
    result.append(numbers1[left])
    left += 1

while right < len(numbers2):
   
    result.append(numbers2[right])
    right += 1

print(result)