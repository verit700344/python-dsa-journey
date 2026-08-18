text = "apple ant banana animal orange"
target = "a"
words = text.split()

count = 0
for word in words :
    if word[0] == target:
        count += 1
print(count)
