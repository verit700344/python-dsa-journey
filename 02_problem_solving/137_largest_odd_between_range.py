numbers = [3, 8, 11, 14, 17, 20, 23, 26]

low = 10
high = 25

largest = 0 

for number in numbers:
    if number >= low and number <= high and number % 2 != 0:
        
        if number > largest:
           
         largest = number
         
print(largest)         
         