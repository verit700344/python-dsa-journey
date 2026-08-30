s = "hello"
stack = []

for char in s:
    stack.append(char)

reversed_string = ""

while stack:
    char = stack.pop()
    reversed_string += char

print(reversed_string)