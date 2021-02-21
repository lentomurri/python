def mysplit(strng):
    myspace = 0
    lst = []
    strng = strng.strip()
    if strng == "":
        return lst 
    newstr = strng[:]
    for char in newstr:
        if ord(char) == 32:
           current = newstr.index(char)
           lst.append(newstr[myspace:current])
           newstr = newstr[current +1 :]
    lst.append(newstr)
    return lst
    


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
