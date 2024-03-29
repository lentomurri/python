#! usr/bin/env python3

# The program updates or saves in the clipboard a particular list of key-values.
#It can be used as a very simple username - mail storage.
import sys, shelve, pyperclip

shelfFile = shelve.open(r"path_to_folder")

def multiclipboard():
        if len(sys.argv) >= 2:
            action = sys.argv[1].lower()
            if action == "list" and len(sys.argv) == 2: 
                # list all keywords in file
                print(list(shelfFile.keys()))
                pyperclip.copy(str(list(shelfFile.keys())))
                wait = input("List saved to clipboard. Press any key to continue")
            elif action == "save" and len(sys.argv) == 3:
                shelfFile[sys.argv[2]] = pyperclip.paste()
            # store text in the keyword
            elif len(sys.argv) == 2:
                shelfFile[action] = pyperclip.copy()
                wait = input("ciao")
        else:
            print(r''' To use the program insert these commands in the terminal
                "list" will return a list of the keywords
                "save" followed by a "keyword" will store the copied text in a specific keyword
                "keyword" will retrieve the text saved in the specified keyword
            ''')
            wait = input("Press any key to continue")

multiclipboard()
