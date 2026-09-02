def countWords(sentence, word):
    sentence = sentence.lower()
    word = word.lower()

    count = 0
    for i in range(len(sentence) - len(word) + 1):
        if sentence[i:i+len(word)] == word:
            count += 1

    return count

def main():
    sentence = input()
    word = input()
    print(countWords(sentence, word))

if __name__ == "__main__":
    main()