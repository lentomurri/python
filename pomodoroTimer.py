#! python3

# takes input from user: how many minutes 
    # sys.argv
# creates countdown
# alerts when times ends
# waits for input to shut off

import time, sys
from PIL import Image
from playsound import playsound

# takes mins and secs from users. If users doesn't specify seconds, it's 00.
try:
    userMins = sys.argv[1]
except:
    input("On the command line, please insert minutes, followed by seconds if needed. Press any key to exit. ")
    

try:
    userSecs = sys.argv[2]
except:
    userSecs = "00"
# convert time into seconds
timing = (int(userMins) * 60) + int(userSecs)

def pomodoroTimer(userTime):
    while userTime > -1:
        # constantly modifies mins and secs
        mins, secs = divmod(userTime, 60)
        #creates current time
        currentTime = "{:02d}:{:02d}".format(mins, secs)
        #waits for one second, then goes down one sec
        time.sleep(1)
        userTime -= 1
        print(currentTime, end="\r")
    # displays image and sound
    finalImg = Image.open(r"C:\Users\Lento\personalBatches\pomodoroTimer.jpg")
    finalImg.show()
    playsound(r"C:\Users\Lento\personalBatches\DNA whistle.mp3")
    

pomodoroTimer(timing)


# time.sleep(1) => will make the timer go down slowly
# divmod(time, 60) => will divide the mins in sixty and give the quotient as seconds