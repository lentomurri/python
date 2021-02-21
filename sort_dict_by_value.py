usr = r"C:\Users\Lento\Desktop\OPEN_UNIVERSITY\basicText.txt"
dct = {}

for i in range(97,122):
    dct[chr(i)] = 0

try:
    tf = open(usr, "r")
    text = tf.read().replace("\n", "")
    for ch in text:
            ch = ch.lower()
            if ch in dct.keys(): 
                dct[ch] += 1    
except Exception as e:
    print(e)

srted = sorted(dct, key = dct.get, reverse = True)

for k in srted:
    print(k, "->", dct[k])