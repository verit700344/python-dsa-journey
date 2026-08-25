def arr_reverse(arr,right,left):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return arr_reverse(arr, right-1, left+1)    
arr = [1,2,3,4,5]
print(arr_reverse(arr, len(arr)-1, 0))  