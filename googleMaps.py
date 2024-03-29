#! python3

#the programs finds automatically a particular location in Google Maps, taking it from the sys.argv
# if the sys.argv is empty, it will take the address from the clipboard

import sys, webbrowser, pyperclip

def searchMap():
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        address = "+".join(sys.argv)
    else:
        try:
            address = pyperclip.paste()
        except:
            print("No address found")
    webbrowser.open(r"https://www.google.com/maps/place/" + address)

searchMap()
