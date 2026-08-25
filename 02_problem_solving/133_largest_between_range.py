numbers = [ 2 , 15 , 8 , 22 , 30 , 12 , 17
           ]
low = 10 
high = 25 

largest = 0
for number in numbers:
    if number >= low and number <= high:
        if number > largest:
            largest = number 
print(largest)