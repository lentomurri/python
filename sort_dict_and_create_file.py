from os import strerror
import re

usr = r"C:\Users\Lento\Desktop\OPEN_UNIVERSITY\basicText.txt"
dct = {}

# create list of letters
for i in range(97,122):
    dct[chr(i)] = 0

try:
    tf = open(usr, "r")
    text = tf.read().replace("\n", "") # remove lines 
    tf.close()
    for ch in text: # if character is a letter: updates counter
            ch = ch.lower()
            if ch in dct.keys(): 
                dct[ch] += 1    
except Exception as e:
    print(e)

srted = sorted(dct, key = dct.get, reverse = True) # sort dict by the values of the key. Reverse = decreasing

write_file = re.search(r"(\d*\D*)\.", usr).group(1) + "-hist.txt" # regex to create file in same location and with
# related but different name
write_file = open(write_file, "a") # append mode makes the write get added, not overwritten 

for k in srted:
    write_file.write(k + " -> " + str(dct[k]) + "\n")