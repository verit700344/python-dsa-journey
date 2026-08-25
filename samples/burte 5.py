'''word = "level"

if word[0] == word[4]:      # works only for single and same 
    print("Palindrome")
'''
word = "level"
is_palindrome = True

for i in range(len(word)):
    if word[i] == word[len(word) - 1 - i]:
        is_palindrome = False
        break

print(is_palindrome)