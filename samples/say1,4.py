def second_largest(arr):
    largest =second = -1

    for num in arr:
        if num > largest :
            second =largest 
            largest = num
        elif num >second and num != largest:
            second=num

    return second
print (second_largest([2,3,5,6,7,]))


