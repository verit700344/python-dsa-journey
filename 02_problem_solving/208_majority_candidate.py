
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
candidate = None
count = 0
for num in numbers:
    if count  == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1  
print(f" the majority : {candidate}")