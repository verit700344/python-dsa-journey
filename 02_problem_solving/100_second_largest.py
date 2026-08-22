numbers = [10, 20, 20, 8, 15, 10, 25]

largest = 0
second_largest = 0

for number in numbers:
    if number > largest:
        second_largest = largest
        largest =number
    elif number > second_largest and number!= largest:
        second_largest = number
        
print(second_largest)