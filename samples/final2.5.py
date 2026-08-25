def subset(nums):
    result=[]

    def backtrack(index,path):
        if index == len(nums):
            result.append(path[:])
            return 
        backtrack(index +1,path)

        path.append(nums[index])
        backtrack(index+1,path)
        path.pop()

        backtrack(0,[])
        return result
    
print(subset([1,3]))
