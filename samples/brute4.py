numbers = [4, 5, 1, 2, 1, 5,6, 4]
frequency = {}
non_repeat = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
for number in numbers:
    if frequency[number] == 1:
        print(number)
        #break # for first non repeat

