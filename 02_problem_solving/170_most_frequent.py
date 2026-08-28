numbers = [4, 5, 4, 6, 5, 7, 6]
frequency = {}
largest_count = 0
most_frequent = None
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
for number in numbers:
    if frequency[number] > largest_count  :
        largest_count = frequency[number]
        most_frequent =  number
print(most_frequent)
        
        