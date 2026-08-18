text = "programming"
result = " "
seen = set()
for char in text:
    if char  not in seen:
        result = result + char
        seen.add(char)
print(result)