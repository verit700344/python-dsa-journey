numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
minimum = numbers[0]
maximum_difference = 0

for number in numbers[1:]:
    difference = number - minimum

    if difference > maximum_difference:
        maximum_difference = difference

    if number < minimum:
        minimum = number
print("Maximum difference:", maximum_difference)