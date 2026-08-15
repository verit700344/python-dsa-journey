numbers = [10, 3, 7, 20, 5]
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest :
        largest = number 
    if number < smallest:
        smallest = number
difference = largest - smallest
print(difference) 
        
    