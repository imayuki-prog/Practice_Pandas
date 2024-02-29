import pandas as pd
import openpyxl
import os
import matplotlib.pyplot as plt

'''
##Path 
################################
pd.options.display.float_format = '{:.2f}'.format
from pathlib import Path
bulk_excel = Path("2024-02-ca")
bulk_excel_path = bulk_excel / '2024-02-ca.xlsx' #loop
dir_list_bulk_excel = os.listdir(bulk_excel)

bulk_csv = Path("2024-02-ca")
bulk_csv_path = bulk_csv / f"{dir_list_bulk_excel[0][0:10]}.csv" 
dir_list_bulk = os.listdir(bulk_csv)
#print(dir_list_bulk[0])
################################

df_bulk = pd.read_csv(f"{bulk_csv_path}")

dfs = {}

for i in range(24):
    df = df_bulk.copy()
    df.rename(columns ={'Unnamed: 0': f"ID_{i}"}, inplace = True)
    dfs[f"ID_{i}"] = df
    #dfs.append(df)

print(dfs['ID_13'])
'''

df = pd.DataFrame(data=range(0, 24))
print(df)