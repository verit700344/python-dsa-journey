text = "hello world"
count = 0
for char in text:
    if char.isalpha() and char not in "aeiou":
        count += 1
print(count)
text = "hello world python"
count = 0

