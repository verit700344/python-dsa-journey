def lon_com(st):
    if not st:
        return ""   
    prefix = ""
    for i in range(len(min(st,key=len))):
        char = st[0][i]
        if all(s[i] == char for s in st):
            prefix += char
        else:
            break   
    return prefix
print(lon_com(["flower","flow","flight"]))