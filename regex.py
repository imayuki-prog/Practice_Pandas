test = {'2024-02-26':{'test', 'even', 'ate', 'ggg', 'even'}}
set_list = list(test['2024-02-26'])[3]
print(set_list)

import pandas as pd

# Sample sales data (you can replace this with your actual data)
data = {'Date': pd.date_range(start='2024-01-01', end='2024-03-31', freq='D'),
        'Sales': [100, 150, 200, 180, 120, 160, 140, 190, 210, 180, 220, 250, 230, 
                  200, 180, 220, 240, 260, 300, 280, 270, 290, 310, 320, 350, 330, 
                  310, 340, 360, 380, 400, 420, 440, 460]}

df = pd.DataFrame(data)

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Group by week starting from Sunday to Monday (W-SUN to W-MON) and calculate the weekly sum
weekly_sales = df.groupby(pd.Grouper(freq='W-SUN', closed='left', label='left')).sum()

# Add a column for week ending date (assuming week ends on Saturday)
weekly_sales['Week Ending'] = weekly_sales.index + pd.DateOffset(days=6)

print(weekly_sales)