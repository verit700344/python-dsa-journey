text = "cat dog hat apple"
target = "t"
words = text.split()
count = 0
for word in words:
    if word[-1] == target:
        count += 1
print(count)