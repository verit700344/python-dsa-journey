import heapq
from multiprocessing import heap

def largest_k(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heapreplace(heap, arr[i])
        return heap
print(largest_k([3, 1, 5, 12, 2, 11, 7], 3)) 