#! python3
import re, pyperclip

data = pyperclip.paste()

passwordCheck = re.compile(r'''
^(?=.{8,16}) #check length of word
(?=.*[a-z]) #check for lower character
(?=.*[A-Z]) #check for upper character
(?=.*[\d]) #check for number
(?=.*[@#$%^&+=]).*$ # check for at least one special character
''', re.VERBOSE)

result = re.findall(passwordCheck, data)

if result == []:
    print('''
    Passwords have to be between 8 and 16 characters long, 
    have at least one lowercase and uppercase character, 
    one number and one special character among @#$%^&+=''')

print("The password is strong, may the Force be with you")