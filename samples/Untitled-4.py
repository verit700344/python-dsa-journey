def max_channels(intervals):
    intervals.sort(key=lambda x:x[1])
    count =1
    last_end=intervals[0][1]
    for start,end in intervals[:1]:
        if start<=last_end:
            count+=1
            last_end =end 
        return count