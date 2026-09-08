numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
alternate_numbers = []
 # positive and negative alternate
positive = []
negative = []
for number in numbers:
    if number >= 0:
        # put it in positive
        positive.append(number)
    else:
        # put it in negative
        negative.append(number)
for i in range(min(len(positive), len(negative))):
    alternate_numbers.append(positive[i])
    alternate_numbers.append(negative[i])