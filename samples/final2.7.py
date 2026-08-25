def permutation(nums):
    result =[]

    def backtrack(path,remaining):
        if not remaining :
            result.append(path)

            return
        for i in range (len(remaining)):
            backtrack(path+[remaining[i]],remaining[:i] + remaining[i+1:])

    backtrack([],nums)
    return result
print(permutation([3,3,7,3]))
