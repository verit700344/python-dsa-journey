numbers = [2, 7, 11, 15]
target = 5
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if abs(numbers[i] - numbers[j]) == target :
            print(numbers[i],numbers[j])