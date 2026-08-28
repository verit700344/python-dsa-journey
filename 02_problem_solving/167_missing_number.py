numbers = [1, 2, 3, 5, 6]

n = len(numbers)+ 1
expected = n * (n + 1) // 2

total = 0

for number in numbers:
    total += number
missing_number = expected - total
print(missing_number)
    
     
     