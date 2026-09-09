parts = input("Enter intervals separated by commas: ").split(",")

intervals = []

for part in parts:
    part_numbers = list(map(int, part.split()))
    intervals.append(part_numbers)

intervals.sort()

merged = [intervals[0]]

for interval in intervals[1:]:
    if interval[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], interval[1])
    else:
        merged.append(interval)

print("Merged intervals:", merged)