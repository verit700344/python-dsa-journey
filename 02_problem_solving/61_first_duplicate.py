numbers = [4, 7, 2, 7, 9, 2]
seen =set()
for number in numbers:
    if number in seen:
        print(number)
        break
    else:
        seen.add(number)