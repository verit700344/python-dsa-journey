numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
missing = len(numbers)
for index, number in enumerate(numbers):
    
        missing = missing ^ index ^ number
        
print(f"The missing number is: {missing}")