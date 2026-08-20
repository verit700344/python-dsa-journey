numbers = [3, 8, 5, 12, 7, 10, 15]


largest_even = 0


for number in numbers:
    if number % 2== 0:
        if number > largest_even:
            largest_even = number


print(largest_even)