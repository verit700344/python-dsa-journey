numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
current = 0
maximum = 0
for number in numbers:
    if number ==  1:
        current += 1
    elif number == 0:
        if current > maximum:
            maximum = current
        current = 0
print(max(maximum, current))