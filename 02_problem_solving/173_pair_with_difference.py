numbers = [8, 1, 5, 3, 10, 6]
target = 2
seen = set()

for number in numbers:
    needed =  number - target

    if needed in seen:
        print(needed ,number)
        break
    else:
        seen.add(number)