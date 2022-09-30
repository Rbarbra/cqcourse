import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8],index=["A","B","C","D","E","F"])
df = pd.DataFrame(np.random.randn(4,6), index=["Test1","Test3","Test2","Test4"], columns=["A","B","C","D","E","F"])

print(s)
print(df)

print(s.iloc[4])
print(s.loc["E"])

print(df.iloc[3][2])
print(df.loc["Test4","C"])

print(df.iloc[3][:])
print(df.iloc[:,2])

print(df.loc["Test4",:])
print(df.loc[:,"A"])
