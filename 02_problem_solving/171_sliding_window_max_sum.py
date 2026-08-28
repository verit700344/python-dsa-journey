numbers = [2, 1, 5, 1, 3, 2]
k = 3
window_sum = 0
largest = 0
for i in range(k) :
    
    window_sum += numbers[i]
    largest = window_sum
for i in range(k,len(numbers)):

    window_sum = window_sum - numbers[i-k] + numbers[i]
    if window_sum > largest:
       largest = window_sum
print(largest)