#! python3

# The program will:
# search for American Style Dates file name 
#replace them with European Dates

import re, os
from pathlib import Path

def searchRegex(fileDirectory):
    # regex for search
    americanRegex = re.compile(r"(0[1-9]|1[0-2])\-([0-2][0-9]|3[0-1])\-[1-2][0-9]{3}\.\w+")
    if os.path.isdir(fileDirectory):
        for item in os.listdir(fileDirectory):
            matching = re.match(americanRegex, item)
            if matching != None:
                europeanString = item.split("-")
                europeanString[0] = matching.group(2)
                europeanString[1] = matching.group(1)
                europeanString = "-".join(europeanString)
                currentFile = workingFolder + "\\" + item
                print(europeanString)
    else:
        print("Please enter a valid folder")
            
if name == "__main__":
    searchRegex(fileDirectory)
