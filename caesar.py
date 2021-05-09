#!/usr/bin/env python3

#Caesar cypher game. It can be upgraded entering a user input for the sentence as well.

user = "The die is cast"
result = []

while True:
    try:
        num = int(input("Please enter a number between 1 and 25: "))
        if num < 1 or num > 25:
            print("{Please enter a valid number")
        else:
            break
    except:
        print("Please enter a valid number")

for char in user:
    if not char.isalpha():
        result.append(char)
    else:
        current = ord(char) + num 
        if ord(char) <= 90:
            if ord(char) + num > 90:
                current = 65 + ((ord(char) + num) % 91)
        elif ord(char) >= 97:
            if ord(char) + num > 122:
                current = 97 + ((ord(char) + num) % 123)
        result.append(chr(current))
        
result = "".join(result)

print(result)
        
