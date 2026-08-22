numbers1 = [1,2,3,4,5,6]
numbers2 = [3,5,7,9]
common = []
for number in numbers1 :
   if number in  numbers2 :
       common.append(number)
print(common)