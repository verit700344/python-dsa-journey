numbers = [2, 4, 7, 9]
target = 13
found = False
for i in range(len(numbers)):
  for j in range(i+1,len(numbers)):
      if numbers[i] + numbers[j] == target:
            found = True
            break

  if found:
        break

if found:
    print("pair exists")
else:
    print("no pair")