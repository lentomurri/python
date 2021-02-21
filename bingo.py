from random import sample 
from time import sleep

list = [i for i in range (1,11)]
print(list)
bingo = sample(list, 5)

for i in bingo: 
    print("Next number is...")
    print(i, end = " \r")
    sleep(2)