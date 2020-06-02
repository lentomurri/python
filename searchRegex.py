#! python3

# This program will ask for a folder where the files are stored.
# It will find all .txt files and apply the regex search the user entered.
# It will display the results in the terminal and even paste them automatically in the clipboard for storage purposes. 

import re, sys, os, pyperclip

# write folder path to access files. enter absolute path.
filePath =  sys.argv[1]

try:
    filedir = os.listdir(filePath)
except:
    print("Invalid path. Please check the provided path is the absolute one.")
    input("Press any key to exit")

print(filedir)

def regexSearch(filedir):
    finalResult = ""
    for item in filedir:
        # the string to find the .txt files
        endTxt = r"[\w]+(\.txt)$"
        # the string that the user wants to match in the files 
        # CHANGE THIS STRING TO MATCH YOUR REGEX SEARCH.
        matching = r"[\w]+\."
        # if file is a text file
        if re.match(endTxt, item)!= None:
            # search for item in absolute path entered by user
            currentFile = open(filePath + "\\" + item)
            currentFile = currentFile.read()
            # matches all occurrences, indicating which file they come from
            string = item + "\n" + str(re.findall(matching, currentFile))
            # stores all the result together, divided by files
            finalResult += "\n" + string
    # return results and paste them on the clipboard
    pyperclip.copy(finalResult)
    print(finalResult)
    input("The contents have been saved on the clipboard. Press any key to exit")

regexSearch(filedir)