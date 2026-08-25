def subset(arr):
    result =[]
    def backtrack(index,current):
        if index==len(arr):
            result.append(current[:])
            return
        backtrack(index+1,current)
        current.append(arr[index])
        backtrack(index+1,current)
        current.pop()
    backtrack(0,[])
    return result
    
print(subset([1,2]))
