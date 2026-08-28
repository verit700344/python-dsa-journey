numbers = [1, 3, 4, 2, 2]
seen = set()
for number in numbers:
    if number in seen:
        print(number)
        break
    else:
        seen.add(number)