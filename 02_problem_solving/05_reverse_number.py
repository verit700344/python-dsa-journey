number = 12345
reversed =  0

while number > 0 :
    digit = number % 10
    reversed = (reversed * 10) + digit
    number = number // 10
print(reversed)
    