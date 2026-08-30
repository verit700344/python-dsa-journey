text = "abbcbbb"
frequency ={}
non_repeating = 0


for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

for char in text :
    if frequency[char] == 1:
     print(char)
     break