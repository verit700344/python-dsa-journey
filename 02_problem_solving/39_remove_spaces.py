text = "hello world python"
result = ""

for char in text:
    if char != " ":
        result = result + char

print(result)