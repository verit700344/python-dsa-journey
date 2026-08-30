text = "hello"

seen = set()

for char in text :
    if char in seen :
        print("duplicate found")
        break 
    else:
         seen.add(char)
