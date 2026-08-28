numbers = [4, 7, 1, 9, 3]
target = 10
seen = set()

for number in numbers:

    needed = target - number

    if needed in seen:
        print(needed, number)
        break
    else :
        seen.add(number)