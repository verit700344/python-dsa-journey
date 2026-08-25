def move_zeror(arr):
    pos= 0

    for num in arr:
        if num != 0:
           arr[pos]=num
           pos+=1

    while pos < len(arr):
              arr[pos] = 0
              pos += 1
    return arr
print(move_zeror([0, 1, 0, 3, 12]))
