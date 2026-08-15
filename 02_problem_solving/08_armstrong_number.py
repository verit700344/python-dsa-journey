number = 153
original = number
total = 0

while number > 0:
    digit = number % 10

    total  = total + (digit ** 3)

    number = number // 10
if original == total :
    
  print("Armstrong")
else :
    print("Not Armstrong")