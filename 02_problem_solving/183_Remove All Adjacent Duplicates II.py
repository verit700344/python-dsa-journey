s = "deeedbbcccbdaa"
k = 3
stack = []
for char in s:
    if not stack or stack[-1][0] != char:
        stack.append((char, 1))
    else :
        count = stack[-1][1]
        stack[-1] = (char,count+1)
    
print(stack)