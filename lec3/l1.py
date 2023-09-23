import pandas as pd
columns=["A","B"]
row=[
    [1,2],
    [3,4],
    [5,6]
]
df=pd.DataFrame(columns=columns,data=row)
df["A"]=["amjad","10",8]
print(df["A"].head())
print(df.describe())
print(df.info)
