numbers = [2, -4, 0, 7, -1, 0, 5, -3]
positive = 0
negative = 0
zero = 0
for number in numbers:
    if number > 0 :
        positive = positive + 1
    elif number < 0:
        negative = negative + 1
    else:
        zero = zero + 1
        
print(positive)
print(negative)
print(zero)    