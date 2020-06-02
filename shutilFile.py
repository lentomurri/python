import shutil, os, re

listFile = os.listdir(r"C:\Users\Lento\personalBatches")

for item in listFile:
    if re.match(r"\w+\.\w+", item):
        shutil.copy(r"C:\Users\Lento\personalBatches\\" + item, r"C:\Users\Lento\Desktop\SelfTaught\tstp\python")

