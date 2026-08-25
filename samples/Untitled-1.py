def cost_for_pattern(arr,odd_first):
    mismatches = 0
    for i,val in enumerate(arr):
        if (i % 2 == 0) != (val % 2 == 0):
            mismatches += 1
    reurn mismatches //2

arr = [1,2,3,4,5,6]
odd_first_cost = cost_for_pattern(arr, 1)
even_first_cost = cost_for_pattern(arr, 0)
print("cost if odd-first:", odd_first_cost )
print("cost if even-first:", even_first_cost)