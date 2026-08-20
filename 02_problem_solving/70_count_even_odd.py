numbers = [1, 2, 3, 4, 5, 6, 8]
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)