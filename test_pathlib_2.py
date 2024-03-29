import pandas as pd
from pathlib import Path
import time


p = Path.cwd() # / "-workspace"
all_files =[]
for i in p.rglob('*.*'):
    all_files.append((i.name, i.parent, time.ctime(i.stat().st_ctime)))

print(all_files)

columns = ["File_name", "Parent", "Created"]
df = pd.DataFrame.from_records(all_files, columns=columns)
df = df[~df["File_name"].str.contains(".csv") == False]
df = df[df["Parent"].astype(str).str.contains("2024-sales-test")] # "Parent" is "Path" object therefore it needs to convert to "Strings"
print(df)
print(df['File_name'])