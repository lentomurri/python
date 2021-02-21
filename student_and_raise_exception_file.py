import re
from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    # Write your code here.
    def __init__(self, message = "The data is invalid"):
        self.message = message
    def __str__(self):
        return self.message

class FileEmpty(StudentsDataException):
    # Write your code here.
    def __init__(self, message = "The file is empty"):
        self.message = message
    def __str__(self):
        return self.message
        
def fileCheck(file):
    try:
        fle = open(file, "r")
        fle = fle.read()
        if len(fle) < 5:
            raise FileEmpty
            fle.close()
    except FileNotFoundError as e:
        print(strerror(e.errno))

def student():
    user = input("Insert path of the file: > ")
    user = user.replace('"', '')
    fileCheck(user)
    text = open(user, "r")
    dct = {}
    while True:
        line = text.readline()
        if line == "":
            break
        try:
            result = re.match(r"^([a-zA-Z]*\s[a-zA-Z]*)\s(\d+\.*\d*)$", line)
            if result == None:
                raise BadLine
        except BadLine as e:
            print(e)
            continue
        studentName = result.group(1).replace("\t", " ")
        mark = result.group(2)
        if studentName not in dct.keys():
            dct[studentName] = float(mark)
        else:
            dct[studentName] += float(mark)
    return dct

result = student()

print(result)