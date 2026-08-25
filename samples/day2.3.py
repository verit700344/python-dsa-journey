def majority_element(arr):
    count = 0
    candidate = None
    for num in arr:
        if count ==0 :
            candidate = num
        count+=1 
        if num != candidate:
            count -=1       

    return candidate
print(majority_element([3,2,3]))