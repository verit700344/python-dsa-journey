s = "aabbcdde"
frequency = {}

for char in s:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for char in s:
    if frequency[char] == 1:
        print(char)
        break
print(frequency)