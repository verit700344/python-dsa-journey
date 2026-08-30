# Problem: Count vowels and consonants
# Topic: Strings
# Difficulty: Easy

word = "programming"
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for letter in word:
    if letter in vowels:
        vowel_count = vowel_count + 1
    else:
        consonant_count = consonant_count + 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)