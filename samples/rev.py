'''def largest(arr):
    max=0
    for i in arr:
        if i>max:
            max=i   
    return max
print(largest([1,2,3,4,5,6,7,8,9,10]))'''

def two_sum(arr,target):
   seen=set()
   for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
   return False
print(two_sum([1,2,3,4,5,6,7,8,9,10],10)) 