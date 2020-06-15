#! python3

#creates backup copies in xip files with incremental number as filename.
# with a loop, if the file doesn't already exists, it creates an incremental number copy.

import zipfile, os

def createZipBackup(folder):
    folder = os.path.abspath(folder) # transforms folder in absolute
    number = 1 #starting number. It will increase if the archive already exists
    while True:     
        filename = "copyBatch" + str(number) + ".zip"
        if os.path.exists(os.path.join(folder, filename)): # the loop will go on only if path doesn't exists. Increase the number and restart.
            number +=1
        else:
            # creates zipfile and places into working folder
            newZip = zipfile.ZipFile(os.path.join(folder, filename), "a")
            for foldername, subfolders, filenames in os.walk(folder):
                # relpath: avoids creating the entire root
                foldername = os.path.relpath(foldername)
                # creates folder inside zip, keeping the structure
                newZip.write(foldername)
                # every file will fit into the correct folder.
                for files in filenames:
                    if not files.startswith("copyBatch") and not files.endswith(".zip"):
                        newZip.write(os.path.join(foldername, files))
            break

createZipBackup(r"C:\Users\Lento\personalBatches\text")