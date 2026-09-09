numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
candidate1 = None
candidate2 = None

count1 = 0
count2 = 0
count_candidate1 = 0
count_candidate2 = 0

for num in numbers:
    if candidate1 is not None and num == candidate1:
        count1 += 1
    elif candidate2 is not None and num == candidate2:
        count2 += 1
    elif count1 == 0:
        candidate1 = num
        count1 = 1
    elif count2 == 0:
        candidate2 = num
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1
for num in numbers:
    if num == candidate1:
        count_candidate1 += 1
    elif num == candidate2:
        count_candidate2 += 1
if count_candidate1 > len(numbers) // 3:
    print(candidate1)

if count_candidate2 > len(numbers) // 3:
    print(candidate2)