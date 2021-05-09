import shutil, os, re
from pathlib import Path
from send2trash import send2trash as stt

workingDirectory = r"enter_your_path"
os.chdir(workingDirectory)
listFile = os.listdir(workingDirectory)

# image regex search: [\w\W]+(\.jpg|\.jpeg|\.psd|\.png)$ // folder: jpg folder
# text regex search: 
# text regex search: [\w\W]+(\.pdf|\.txt)$ // folder: pdf folder

for item in listFile:
    if re.match(r"[\w\W]+(\.py)$", item, re.IGNORECASE):
        # print(item)
        shutil.copy(Path(item).absolute(), r"enter_path")
        # optional: delete the copied file. Can be omitted for extra safety. 
        stt.send2trash(item)

