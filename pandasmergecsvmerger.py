import pandas as pd


df1 = pd.read_csv("firstfile.csv")
df2 = pd.read_csv("secondfile.csv")
merged = df1.merge(df2, on="header", how="outer").fillna("-")
merged.to_csv("merged.csv", index=False)
