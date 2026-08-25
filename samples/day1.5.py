def two_sum(arr,targ):
    values={}
    for num in arr:
        if targ-num in values:
            return (targ-num,num)
        values[num]=True
    return None
if __name__ == "__main__":
    print(two_sum([10,15,3,7],17))