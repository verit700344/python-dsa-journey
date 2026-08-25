def activity_select(start,end):
    avtities=list(zip(start,end))
    avtities.sort(key=lambda x:x[1])    

    count=0
    last_end= avtities[0][1]
    for i in range(1,len(avtities)):
        if avtities[i][0]>=last_end:
            count+=1
            last_end=avtities[i][1]     
    return count+1
print(activity_select([1,3,0,5,8,5],[2,4,6,7,9,9]))  # Output: 4