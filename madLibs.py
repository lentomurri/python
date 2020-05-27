#! python3

# Program takes a text
# It substitutes the word NOUN, ADJECTIVE, VERB with actual user inputs

import re

text = "The ADJECTIVE panda walked to the NOUN and then VERB! A nearby NOUN was unaffected by these events."

# function takes a text
def madLibs(chosenText):
    chosenText = re.split(r"(\W)", text)
    # creates list to find words to sub
    subs = ["ADJECTIVE", "NOUN", "VERB"]
    for i, word in enumerate(chosenText):
        if word in subs:
            # asks user for specific input
            sub = input("Please enter your " + word.lower() + ": ")
            # subs word by using index counter
            chosenText[i] = sub
    #joins the text back
    chosenText = "".join(chosenText)
    print(chosenText)

madLibs(text)



