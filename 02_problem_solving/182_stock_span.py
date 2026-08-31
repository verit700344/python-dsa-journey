prices = [100, 80, 60, 70, 60, 75, 85]

stack = []
span = [0] * len(prices)

for i in range(len(prices)):
    while stack and prices[stack[-1]] <= prices[i]:
       span[i] = prices[stack[-1]]
       stack.pop()
    if not stack:
        span[i] = i + 1
    else:
        span[i] = i - stack[-1]
    stack.append(i)
print(stack)