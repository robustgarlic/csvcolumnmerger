import pandas as pd
from datetime import datetime

#start time for script
start_time = datetime.now()

df1 = pd.read_csv("first_file.csv")
df2 = pd.read_csv("second_file.csv")

def dataframe_difference(df1, df2, which=None):
    comparison_df = df1.merge(df2, on = 'Header_Here',
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    #diff_df.to_csv('diff.csv')
    return diff_df

netbrain_only = dataframe_difference(df1, df2, which='left_only')
netbrain_only.to_csv('NewFileMatching_left.csv', index=False)
spectrum_only = dataframe_difference(df1, df2, which='right_only')
spectrum_only.to_csv('NewFileMatching_right.csv', index=False)
both = dataframe_difference(df1,df2, which='both')
both.to_csv('NewFileMatchingBoth.csv', index=False)
print("\nElapsed time: " + str(datetime.now() - start_time))

