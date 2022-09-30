import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
df = pd.DataFrame(np.random.randn(4,6), index=["Test1","Test2","Test3","Test4"], columns=["A","B","C","D","E","F"])

print(s)
print(df)

print(type(s))
print(type(df))
#sorting the original to create 6 new DataFrame.
print(df.sum())
print(df.describe())
print(df.sort_index(axis=1,ascending=False))
print(df.sort_values(by="B"))
print(df.index)
print(df.columns)
#let the program print a description of the original DataFrame
print(list(df.index))
print(list(df.columns))
