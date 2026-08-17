text = "madam"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text
if reversed_text == text :
        print("palindrome")
else:
    print("notpalindrome" )