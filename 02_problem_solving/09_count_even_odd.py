
numbers = [12, 7, 4, 9, 10, 15, 8]

even = 0
odd = 0

for number in numbers:
    if number  % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(even)
print(odd)