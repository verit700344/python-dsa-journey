def countChar(data, ch):
    count = 0
    for c in data:
        if c == ch:
            count += 1
    return count

def main():
    data = input()
    ch = input()
    print(countChar(data, ch))

if __name__ == "__main__":
    main()