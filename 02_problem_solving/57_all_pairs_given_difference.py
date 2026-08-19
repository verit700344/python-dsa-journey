numbers =[ 1 ,1 ,2, 3, 7 ,4, 7 ,5 , 6, 6]
target = 4
for i in range (len(numbers)):
   for j in range (i+1 ,len(numbers)):
       if abs(numbers[i] - numbers[j]) == target:
           print(numbers[i],numbers[j])