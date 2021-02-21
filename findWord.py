def findme(word1, word2):
    index = 0
    for i in word1:
        word2 = word2[index:]
        if i not in word2:
            return False
        index = word2.index(i)
    return True

print(findme("dog", "vcxzxdcybfdstbywuefsas"))