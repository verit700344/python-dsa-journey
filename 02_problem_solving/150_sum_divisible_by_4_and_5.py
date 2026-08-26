numbers = [4, 5, 10, 15, 20, 25, 30, 40]
total = 0

for number in numbers:
   if number % 4 == 0 and number % 5 == 0:
       
       total += number
print(total)