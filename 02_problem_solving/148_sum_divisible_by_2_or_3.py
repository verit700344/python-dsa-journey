numbers = [4, 6, 7, 9, 10, 11, 12, 13]
total = 0

for number in numbers:
   if number % 2 == 0 or number % 3 == 0:
       
       total += number
print(total)