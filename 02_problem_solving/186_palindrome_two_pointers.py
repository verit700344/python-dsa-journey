s = "racecar"
left = 0 
right = len(s) - 1 
while left < right:
    if s[left] != s[right]:
        print("Not a palindrome")
        break
    left += 1
    right -= 1
else:
    print("Is a palindrome")