def frq_count(s):
    frequency ={}
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency    

if __name__ == "__main__":
    
    print(frq_count("hello world"))   