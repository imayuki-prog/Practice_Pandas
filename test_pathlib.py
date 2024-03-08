import pandas as pd
import os
from pathlib import Path

parts = ["in", "input.xlsx"]
in_file_1 = Path.cwd().joinpath(*parts)
out_file_1 = Path.cwd()

print(in_file_1)
print(out_file_1)

folders = []
files = []

dir_to_scan = r"/Users/yoshi/-workspace" # Current dir must be "C:/Users/yoshi/-workspace"
p = Path(dir_to_scan)
for entry in os.scandir(p):
    if entry.is_dir():
        folders.append(entry)
    elif entry.is_file():
        files.append(entry)

print(folders)
print(files)


#Extract dir and files
'''
for dirName, subdirList, fileList in os.walk(p):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
'''

#Extract a list under the current dir. 
for i in p.glob('*.*'):
    print(i.name)

### prints out the file in the top level directory.
'''
for i in p.glob('**/*.*'):
    print(i.name)
'''

for i in list(p.rglob('*.csv')):
    print(i.name)
