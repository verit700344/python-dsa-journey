numbers = [10, 20, 30, 40, 50]
target = 26
farthest = numbers[0]
for number in numbers :
    if abs(number - target) > abs(farthest - target):
        farthest = number 
print(farthest)