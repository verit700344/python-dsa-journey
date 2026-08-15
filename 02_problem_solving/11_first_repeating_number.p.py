numbers = [4, 5, 1, 2, 1, 5, 4]
seen = set()
for number in numbers:
    if number in seen:
        
        print(number)
        break
        
    else:
        
       seen.add(number)

