s = "3+2*2"

stack = []
number = 0
operator = '+'

for char in s:

    if char.isdigit():
        number = number * 10 + int(char)

    else:
        number = number * 10 + int(operator)