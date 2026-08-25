


def permutation(num):
    result=[]

    def backtrack(path,remaining):
        if not remaining:
            result.append(path)
        for i in range(len(remaining)):
            backtrack(path+ [remaining[i]],remaining[:i]+remaining[i+1:])
    backtrack([],num)
    return result
print(permutation("abc"))