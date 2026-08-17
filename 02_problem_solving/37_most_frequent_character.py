text = "programming"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
largest = 0
most_frequent = ""

for char in frequency:
    if frequency[char] > largest:
        largest = frequency[char]
        most_frequent = char

print(most_frequent)