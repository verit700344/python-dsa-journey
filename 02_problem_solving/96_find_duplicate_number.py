numbers = [1, 2, 3, 4, 3, 5]

seen = set()

for number in numbers:
    if number in seen:
        print(number)
        break
    else:
        seen.add(number)