def largest_element(arr):
    max=arr[0]
    for num in arr:
        if num > max:
            max=num
    return max 
arr =[2,4,6,7]
print(largest_element(arr))