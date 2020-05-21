#!/usr/bin/python3
import re, pyperclip, subprocess

data = pyperclip.paste()

phoneNumbercheck = re.compile(r'''
(?:\d{3}|\(\d{3}\))? # optional area code UK
(?:-|\s\d{3,4}){2,3} #in case there is no area code, it will return only 2 blocks of 3
''', re.VERBOSE)

emailCheck = re.compile(r'''
[^\.\w]\w+[!#\$%&'\*\+-/=\?\^_`{\|}~]*(?:\.\w+)?(?:\".*\")?\w*@\w+\.\w+
''', re.VERBOSE)

result = re.findall(emailCheck, data)
result2 = re.findall(phoneNumbercheck, data)

stringResult = "Email:\n"
stringResult2 = "\nTelephone:\n"

if result != []:
    for email in result:
        stringResult += email + "\n" 

if result2 != []:
    for phone in result2:
        stringResult2 += phone + "\n"

pyperclip.copy(stringResult + stringResult2)
subprocess.Popen([r'C:\WINDOWS\system32\notepad.exe'])
