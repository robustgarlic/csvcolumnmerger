import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_csv('t1s.csv')
df2 = pd.read_csv('tomhunter.csv')

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = 'circuitid')
df3.set_index('circuitid', inplace = True)

# Write it to a new CSV file
df3.to_csv('resultsthatmatch.csv')