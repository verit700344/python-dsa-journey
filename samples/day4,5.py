def check_sub(arr,target):
    def dfs(i,current_sum):
        if current_sum == target:
            return True
        
        if i >= len(arr) or current_sum > target:
            return False
        return (dfs(i+1,current_sum +arr[i]) or dfs(i+1,current_sum))
    return dfs(0,0)
print(check_sub([2,3,4,4],8))