def reverse_arr(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_arr(arr,left+1,right-1)

arr=[4,5,5,]
reverse_arr(arr,0,len(arr)-1)
print(arr)