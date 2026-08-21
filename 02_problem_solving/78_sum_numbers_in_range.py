numbers = [2, 5, 8, 12, 15, 18, 20]
low = 8
high = 18
total =0
for number in numbers :
    if number >= low and number <= high:
        total+= number
        
print(total)