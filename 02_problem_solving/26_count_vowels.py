text = "hello world"
count = 0

for char in text:
    if char in  "aeiou":
        count += 1

print(count)