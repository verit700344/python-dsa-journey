numbers = [10, 8, 12, 5, 7, 3]
target = 6
last_smaller = None


for number in numbers:
    if number < target:
       last_smaller = number  
print(last_smaller)
        