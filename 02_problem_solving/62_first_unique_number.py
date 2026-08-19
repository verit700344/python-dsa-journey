numbers = [4, 7, 2, 7, 9, 2]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] +=1 
    else:
        frequency[number] =1

for number in numbers:
    if frequency[number]== 1:
      print(number)
      
      break