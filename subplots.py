import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# dataframe sample data
df1 = pd.DataFrame(np.random.rand(10,2)*100, columns=['A', 'B'])
df2 = pd.DataFrame(np.random.rand(10,2)*100, columns=['A', 'B'])
df3 = pd.DataFrame(np.random.rand(10,2)*100, columns=['A', 'B'])
df4 = pd.DataFrame(np.random.rand(10,2)*100, columns=['A', 'B'])
df5 = pd.DataFrame(np.random.rand(10,2)*100, columns=['A', 'B'])
df6 = pd.DataFrame(np.random.rand(10,2)*100, columns=['A', 'B'])

#define number of rows and columns for subplots
nrow=3
ncol=2

# make a list of all dataframes 
df_list = [df1 ,df2, df3, df4, df5, df6]
fig, axes = plt.subplots(nrow, ncol)

# plot counter
count=0
for r in range(nrow):
    for c in range(ncol):
        df_list[count].plot(ax=axes[r,c])
        count+=1

plt.show