def sum_digit(s):
    sum=0
    while s > 0 :
      sum += s%10
      s//=10
    return sum
print(sum_digit(112))

