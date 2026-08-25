def arr_sort(arr):
    for i in range (len(arr) -1):
        if arr[i]> arr[i+1]:
            return False
    
        return True
print (arr_sort([2,3,5,6,7,]))