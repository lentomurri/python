#! /usr/bin/env python3

#The program checks for two words, returning if they are an Anagram of each other.

def anagram():
    word_1 = input("Word 1: ").lower()
    word_2 = input("Word 2: ").lower()
    word1 = [i for i in word_1]
    word2 = [i for i in word_2]
    word1.sort()
    word2.sort()
    if word1 == word2 : return "Anagram"
    else: return "Not Anagram"

print(anagram())
