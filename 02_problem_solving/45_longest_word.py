text = "I Love Programming "

longest = " "
words = text.split()

for word in words:
   if len(word) > len(longest):
       longest = word
print(longest)
      
