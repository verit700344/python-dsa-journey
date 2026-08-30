

numbers = [0, 1, 0, 3, 12]
position = 0

for i in range(len(numbers)):
   if numbers[i] != 0: 
    numbers[position] = numbers[i]
    position += 1
    
for i in range(position, len(numbers)):
    numbers[i] = 0

print(numbers)
