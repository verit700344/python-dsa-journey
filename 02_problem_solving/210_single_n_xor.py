numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
single = 0
for n in numbers:
    single ^= n
print(f"The single number is: {single}")