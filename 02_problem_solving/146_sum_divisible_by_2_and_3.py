numbers = [6, 8, 9, 12, 15, 18, 20, 24]
total = 0

for number in numbers:
   if number % 2 == 0 and number % 3 == 0:
       
       total += number
print(total)