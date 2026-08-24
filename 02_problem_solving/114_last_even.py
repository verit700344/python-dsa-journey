numbers = [1, 4, 7, 8, 3, 10, 5]

last_even = None

for number in numbers:
    if number% 2 ==0  :
        last_even = number

print(last_even)