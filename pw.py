#! python3
# PASSWORD MANAGER PROJECT
 # command line arguments: takes what we insert in the command line and store them as arguments to be used in the program

import sys, pyperclip, json

with open("C:\\Users\\Lento\\personalBatches\\dict.json", "r") as read_file:
    data = json.load(read_file)
    read_file.close()
#if there's no argument after the sys argument (the name of the file), we remind the user to insert the name of the account they want to
# search the password list for, or they want to enter a new password for

if len(sys.argv) < 2:
    print("Usage: pw " + sys.argv[0] + "[account] - copy account password")
    sys.exit()

account = sys.argv[1]

if len(sys.argv) == 3:
    #use pyperclip to add password to clipboard
        data[account] = sys.argv[2]
        print('Password for ' + account + " saved in dictionary")
        with open("C:\\Users\\Lento\\personalBatches\\dict.json", "w") as write_file:
            json.dump(data, write_file)
        sys.exit()

# if the arg is there
#check if the account is already in password: in that case, return the password

if account in data:
    #use pyperclip to add password to clipboard
    pyperclip.copy(data[account])
    print('Password for ' + account + " copied to clipboard.")
    with open("C:\\Users\\Lento\\personalBatches\\dict.json", "w") as write_file:
            json.dump(data, write_file)
else:
    print("there is no account named " + account)
