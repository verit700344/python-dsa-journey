numbers = [8, 5, 12, 7, 3, 10, 15]
smallest_odd = numbers[0]
for number in numbers:
    if number % 2 != 0:
        if number < smallest_odd:
            smallest_odd =number
print (smallest_odd)
        