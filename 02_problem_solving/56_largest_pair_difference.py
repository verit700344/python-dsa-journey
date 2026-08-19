numbers = [2,4,6,6,7,]
l_diff = 0
for i in range (len(numbers)):
    for j in range (i+1,len(numbers)):
        if numbers[i] - numbers[j] > l_diff:
            diff =abs(numbers[i] - numbers[j])
            l_diff= diff
            
print(l_diff)