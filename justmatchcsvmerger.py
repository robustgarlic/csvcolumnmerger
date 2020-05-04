import pandas as pd


df1 = pd.read_csv('csv1.csv')
df2 = pd.read_csv('csv2r.csv')


df3 = pd.merge(df1, df2, on = 'firstcolumnheader')
df3.set_index('firstcoulumnheader', inplace = True)

# Write it to a new CSV file
df3.to_csv('resultsthatmatch.csv')
