numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

minimum = numbers[0]
maximum_profit = 0
for number in numbers:
    if number < minimum:
        minimum = number
    else:
        profit = number - minimum
        if profit > maximum_profit:
            maximum_profit = profit
            
print("Maximum profit:", maximum_profit)