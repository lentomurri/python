# A little bingo for boring Quarantine time. 
#Little exercise to memorise sample functions.

from random import sample 
from time import sleep

print("Next number is...")

for i in sample([i for i in range (1,90)], 89): 
    print(i)
    sleep(2)
