import pandas as pd


df1 = pd.read_csv("t1s.csv")
df2 = pd.read_csv("tomhunter.csv")
merged = df1.merge(df2, on="circuitid", how="outer").fillna("-")
merged.to_csv("merged.csv", index=False)