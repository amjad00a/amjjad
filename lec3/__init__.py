import pandas as pd
df=pd.read_csv("../lec/diabetes.csv")
print(df.head())
print(df.describe())
print(df.info)
df2=df[["Pregnancies","Age","Outcome"]]
print(df2.head())
print(df2.describe())
df2["new_age"]=df2["Age"]*2
print(df2.head())
print(df2.describe())