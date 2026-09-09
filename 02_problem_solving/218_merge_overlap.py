


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
parts = input("Enter intervals separated by commas: ").split(",")

intervals = []

for part in parts:
    part_numbers = list(map(int, part.split()))
    intervals.append(part_numbers)

print(intervals)
