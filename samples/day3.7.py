import heapq
def merge_k_arrays(arrays):
    heap=[]
    result=[]
    for i in range(len(arrays)):
        heapq.heappush(heap,(arrays[i][0],i,0))
    while heap: 
        val,arr_i,ele_i=heapq.heappop(heap)
        result.append(val)
        if ele_i+1<len(arrays[arr_i]):
            heapq.heappush(
                heap,(arrays[arr_i][ele_i+1],arr_i,ele_i+1)

            )
    return result
print(merge_k_arrays([[1,4,3],[3,5,4],[3,5]]))