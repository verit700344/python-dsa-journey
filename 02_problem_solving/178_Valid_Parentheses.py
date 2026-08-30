s = "({[]})"
stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
for char in s:

    if char in "([{":
        stack.append(char)

    else:
        if not stack or stack[-1] != pairs[char]:
          print(False)
          break
        stack.pop()
else:
    print(len(stack) == 0)