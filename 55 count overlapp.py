def countWords(sentence, word):
    sentence = sentence.lower()
    word = word.lower()

    count = 0
    for i in range(len(sentence) - len(word) + 1):
        if sentence[i:i+len(word)] == word:
            count += 1

    return count

def main():
    sentence = str(input())
    word = str(input())

    result = countWords(sentence, word)
    print(result)

if __name__ == "__main__":
    main()